# SPDX-FileCopyrightText: 2024-present Brandon Rose <rose.brandon.m@gmail.com>
#
# SPDX-License-Identifier: MIT
from typing import TYPE_CHECKING

from archytas.tool_utils import AgentRef, LoopControllerRef, ReactContextRef, tool
from beaker_kernel.lib import BeakerAgent

if TYPE_CHECKING:
    from beaker_kernel.kernel import BeakerKernel


class MimiAgent(BeakerAgent):
    """
    You are a helpful agent that will answer questions and help with what is asked of you.

    """
    # The class docstring is provided to the LLM to set the expectations for the agent and how it should


    # async def setup(self, context_info: dict[str, any], )

    # A sample tool to get you started.
    # Notice that the doc-string provides instructions to the agent about how and when to use the tools along with the
    # expected inputs and outputs, including the datatype what they represent so the agent knows how to prepare proper
    # input and how to use the output of the tool.
    @tool()
    async def search_installed_packages(self, name: str, agent: AgentRef) -> str:
        """
        Search installed packages using a naive match

        E.g. Searching using the name "Data" might return ["DataFrames"]

        Args:
            name (str): this is the name (or part of the name) of the package to find.
        Returns:
            str: List of modules that can be imported with `import`/`using`
        """
        _, _, installed = await agent.context.get_jupyter_context()

    @tool(autosummarize=True)
    async def search_package_registries(self, name: str, agent: AgentRef) -> str:
        """
        Search packages that can be installed using `Pkg.add` using a naive match (occursin)

        It might be worth checking installed packages first.

        E.g. Searching using the name "X" might return ["MimiX"] which is the name of the IAM
        
        you want to install

        Args:
            name (str): this is the name (or part of the name) of the package to find.

        Returns:
            str: List of modules that can be installed using Pkg.add
        """
        code = agent.context.get_code("search_packages", {"module": name})
        response = await agent.context.evaluate(
            code,
            parent_header={},
        )
        return str(response["return"])
    
    @tool(autosummarize=False)
    async def get_model_info(self, model_var_name: str, agent: AgentRef) -> dict:
        """
        Get information about Mimi model parameters and variables and which compartments they belong to.

        You should probably run this before asking the user for more information.

        Args:
            model_var_name (str): Variable name that contains the Mimi model in the REPL

        Returns:
            dict: Information about the Mimi Model  
        """
        code = agent.context.get_code("model_info", {"model": model_var_name})
        response = await agent.context.evaluate(
            code,
            parent_header={},
        )
        return response["return"]


    @tool(autosummarize=True)
    async def retrieve_documentation_for_module(self, package_name: str, agent: AgentRef) -> str:
        """
        Gets the specified module documentation

        Args:
            package_name (str): this is the name of the package to get information about.
        Returns:
            str: Markdown of the module docs
        """
        code = agent.context.get_code("get_module_docs", {"module": package_name})
        response = await agent.context.evaluate(
            code,
            parent_header={},
        )
        return response["return"]
    
    @tool(autosummarize=True)
    async def get_function_docstring(self, function_name: str, agent: AgentRef):
        """
        Use this tool to additional information on individual function such as their inputs, outputs and descrption (and generally anything else that would be in a docstring)
        
        Read the information returned to learn how to use the function and which arguments they take.
        
        The function names used in the input to this tool should include the entire module hierarchy

        If this fails, this means the function does not exist.
        
        Args:
            function_name (str): name of the function to lookup. 
        """
        code = f"""
            import DisplayAs, JSON3
            try {function_name} 
            catch 
                DisplayAs.unlimited(
                    JSON3.write(
                        Dict("docs" => "{function_name} not defined")
                    )
                )
            else
                docstring = string(@doc({function_name}))
                doc_object = Dict("docs" => docstring)
                DisplayAs.unlimited(
                    JSON3.write(doc_object)
                )
            end
        """
        response = await agent.context.beaker_kernel.evaluate(
            code,
            parent_header={},
        )
        docs = response["return"]["docs"]
        return docs

    @tool()
    async def generate_plot_var_code(self, model_name: str, component_name: str, variable_name: str, agent: AgentRef, loop: LoopControllerRef) -> None: 
        """
        Generate the code `Mimi.plot(${model_name}, :${component_name}, :${variable_name})`.

        Once this code is generated, please give it to `submit_custom_code`

        All the information should be found if you run `get_model_info`.

        Args:
            model_name (str): Variable name of the Mimi model in the REPL
            component_name (str): The component of interest
            variable_name (str): The variable to plot INSIDE the component
        """
        code = f"Mimi.plot({model_name}, :{component_name}, :{variable_name})"
        return code