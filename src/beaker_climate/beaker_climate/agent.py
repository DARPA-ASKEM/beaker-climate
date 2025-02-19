import logging
import os
from pathlib import Path
from archytas.tool_utils import AgentRef, LoopControllerRef, ReactContextRef, tool

from beaker_kernel.lib import BeakerAgent
from beaker_kernel.lib.context import BaseContext
import google.generativeai as genai
from google.generativeai import caching
from adhoc_api.tool import AdhocApi
from adhoc_api.loader import load_yaml_api

logger = logging.getLogger(__name__)

class ClimateDataUtilityAgent(BeakerAgent):
    """
    You will be loading catalogs and using the data in them.
    """
    def __init__(self, context: BaseContext = None, tools: list = [], **kwargs):
        self.logger = logger
        super().__init__(context, tools, **kwargs)

        # Load prompt files and set the Agent context
        self.root_folder = Path(__file__).resolve().parent
        prompts_dir = os.path.join(self.root_folder, 'prompts')

        # Read agent.md first
        agent_file = os.path.join(prompts_dir, 'agent.md')
        if os.path.exists(agent_file):
            with open(agent_file, 'r') as f:
                self.add_context(f.read())
        
        # Read remaining .md files
        for file in os.listdir(prompts_dir):
            if file.endswith('.md') and file != 'agent.md':
                with open(os.path.join(prompts_dir, file), 'r') as f:
                    self.add_context(f.read())

        genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))
        
        # Use the already set root_folder
        api_def_dir = os.path.join(self.root_folder, 'api_documentation')

        # Get API specs and directories in one pass
        self.api_specs = []
        api_yaml = Path(os.path.join(api_def_dir, 'noaa_api.yaml'))
        api_spec = load_yaml_api(api_yaml)
        self.api_specs.append(api_spec)

        # Note: not all providers support ttl_seconds
        ttl_seconds = 1800
        drafter_config_gemini={'provider': 'google', 'model': 'gemini-1.5-pro-001', 'ttl_seconds': ttl_seconds, 'api_key': os.environ.get("GEMINI_API_KEY", "")}
        drafter_config_anthropic={'provider': 'anthropic', 'model': 'claude-3-5-sonnet-latest', 'api_key': os.environ.get("ANTHROPIC_API_KEY")}
        specs = self.api_specs

        try:
            self.api = AdhocApi(logger=self.logger, drafter_config=[drafter_config_anthropic, drafter_config_gemini], apis=specs)
        except ValueError as e:
            self.add_context(f"The APIs failed to load for this reason: {str(e)}. Please inform the user immediately.")
            self.api = None

        self.api_list = [spec['name'] for spec in specs]

    @tool()
    async def get_pangeo_catalog_info(self, agent: AgentRef) -> str:
        """
        Fetches names and descriptions of all relevant pangeo catalogs.

        Returns:
            str: All available pangeo catalogs with descriptions.
        """
        response = await agent.context.evaluate("__pangeo_info")
        return response

    @tool 
    async def load_pangeo_catalog(
        self, 
        category: str, 
        dataset: str, 
        agent: AgentRef,
        loop: LoopControllerRef,
        react_context: ReactContextRef
    ) -> str: 
        """
        Loads a catalog from pangeo given a catalog and a category it resides in.
        A catalog's category is found in the catalog info: use the `get_catalog_info` tool if you are not sure.

        If you get a bad request error, inform the user they need to set up Google Cloud Storage authentication,
        as that means the catalog is a 'requester pays' catalog. For more info, tell them to consult the pangeo-datastore 
        GitHub page.

        Args:
            category (str): One of pangeo's categories for catalogs.
            dataset (str): target catalog to be loaded.

        Returns:
            str: The response of loading the catalog.
        """
        code = agent.context.get_code("load_catalog", {"dataset": dataset, "category": category})
        try:
            return await self.tools['run_code'](code, agent=agent, loop=loop, react_context=react_context)
        except Exception as e:
            logger.warning(e)
            return str(e)

    @tool()
    async def inspect_pangeo_catalog(self, catalog: str, agent: AgentRef,
        loop: LoopControllerRef,
        react_context: ReactContextRef) -> str:
        """
        Inspect a catalog for details about it.
        This retrieves all dataset names. 
        Prefer the search tool unless requested.
        
        Args:
            catalog (str): Loaded catalog with load_catalog

        Returns:
            str: The details
        """
        try:
            return await self.tools['run_code'](f"list({catalog}.keys())", agent=agent, loop=loop, react_context=react_context)
        except Exception as e:
            logger.warning(e)
            return str(e) 


    @tool()
    async def search_pangeo(self, catalog: str, keywords: dict, agent: AgentRef) -> list:
        """
        Search the catalog using keywords.
        This returns a list of datasets in the catalog that match.
        You will use this before getting a dataset with get_pangeo_dataset tool.
        
        Args:
            catalog (str): the catalog you've loaded with load_catalog
            keywords (Optional[dict]): Specific search parameter attributes (e.g., variable_id='tas', experiment_id='historical')
                                Valid keys include: 'activity_id', 'experiment_id', 'variable_id', 
                                'source_id', 'table_id', 'grid_label'            

        Returns:
            list: a list of search results by dataset name (converted from a pandas dataframe)
        """
        code = agent.context.get_code("search", {"catalog": catalog, "keywords": keywords})
        response = await agent.context.evaluate(code)
        return response["return"]
    
    
    @tool()
    async def get_pangeo_dataset(self, variable_name: str, name: str, agent: AgentRef) -> str:
        """
        Get a dataset from the prior search and loads it to a given variable.
        This should be used after the search_pangeo tool.
        
        Args:
            variable_name: the target variable name to save the dataset to
            name: the dataset from the search results
        
        Returns:
            str: The dataset, or an error message
        """
        code = agent.context.get_code("get_dataset", {'name': name, "variable_name": variable_name})
        response = await agent.context.evaluate(code)
        return response["return"]

    # @tool
    # async def get_available_values_for_esm_search_attribute(self, catalog: str, attribute: str, agent: AgentRef) -> list[str]:
    #     """
    #     Get available values for a specific attribute.
    #     The attributes available to you are
    #     'source_id'
    #     'member_id'
    #     'experiment_id'
    #     'variable_id'
    #     'grid_label'
    #     'activity_id'
        
    #     Args:
    #         catalog (str): the catalog you've loaded with load_catalog
    #         attribute (str): The attribute to get values for (e.g., 'activity_id', 'variable_id')
            
    #     Returns:
    #         List[str]: List of available values for the attribute
    #     """
    #     code = agent.context.get_code("get_attribute_values", {'catalog': catalog, 'attribute': attribute})
    #     response = await agent.context.evaluate(code)
    #     return response["return"]
    

    @tool()
    async def consult_noaa_psl(self, query: str, agent: AgentRef, loop: LoopControllerRef, react_context: ReactContextRef) -> str:
        """
        This tool is used to ask a question of the NOAA PSL data catalog API. 
        It allows users to ask questions about the catalog and get back information including available datasets and URLs to download specific files.

        If you use this tool, you MUST indicate so in your thinking. Wrap the tool name in backticks.

        Args: 
            query (str): The question you want to ask about the NOAA PSL catalog.

        Returns: 
            str: returns instructions on how to utilize the the NOAA PSL catalog based on the question asked.
        """
        try:
            results = self.api.ask_api("NOAA Physical Sciences Laboratory", query)
            return f"Here is the information I found about how to use the catalog: \n{results}"
        except Exception as e:
            self.logger.error(str(e))
            