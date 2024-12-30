import json
import logging
import re
from typing import Optional
import codecs

import pandas
import matplotlib.pyplot as plt
import xarray as xr

from archytas.react import Undefined
from archytas.tool_utils import AgentRef, LoopControllerRef, ReactContextRef, tool

from beaker_kernel.lib import BeakerAgent
from beaker_kernel.lib.context import BaseContext

from pathlib import Path

logger = logging.getLogger(__name__)

from time import sleep
from .search.esgf_search import ESGFProvider

class ClimateDataUtilityAgent(BeakerAgent):
    """
    You are assisting us in modifying geo-temporal datasets.

    The main things you are going to do are regridding spatial datasets, temporally rescaling datasets, and clipping the extent of geo-temporal datasets.

    If you don't have the details necessary to use a tool, you should use the ask_user tool to ask the user for them.
    """
    def __init__(self, context: BaseContext = None, tools: list = None, **kwargs):
        self.logger = logger
        super().__init__(context, tools, **kwargs)

        documentation_path=Path(__file__).parent / "api_documentation" / "climate_search.md"
        initial_context_msg_added = False
        while not initial_context_msg_added:
            with open(documentation_path, 'r') as f:
                try:
                    self.add_context(f'''\
        The Earth System Grid Federation (ESGF) is a global collaboration that manages and distributes climate and environmental science data. 
        It serves as the primary platform for accessing CMIP (Coupled Model Intercomparison Project) data and other climate model outputs.
        The federation provides a distributed database and delivery system for climate science data, particularly model outputs and observational data.
        Through ESGF, users can search, discover and access climate datasets from major modeling centers and research institutions worldwide.
        The system supports authentication, search capabilities, and data transfer protocols optimized for large scientific datasets.

        If datasets are loaded, use xarray with the OpenDAP URL.
        If the user asks to download a dataset, ask them if they are sure they want to download it.

        Additionally, any data downloaded should be downloaded to the './data/' directory.
        Please ensure the code makes sure this location exists, and all downloaded data is saved to this location.

        Provided below is the comprehensive documentation of the climate-search tools that you have access to.
        ALWAYS reference this when using the climate-search tools.                             
    ```
    {f.read()}
    ```
''')
                    initial_context_msg_added = True
                except Exception as e:
                    sleep(0.5)
        self.esgf = ESGFProvider(self.oneshot)
        
       
    @tool()
    async def search(self, query: str, agent: AgentRef, loop: LoopControllerRef, react_context: ReactContextRef) -> dict:
        """
        This tool searches ESGF for datasets.
        Save the UNMODIFIED JSON output to a variable in the user's notebook.

        Args:
            query (str): The user's query to pass to the climate search tool.
        Returns:
            dict: ESGF unmodified JSON output to be saved to a variable in the notebook.
        """
        try: 
            return await self.esgf.tool_search(query)
        except Exception as e:
            self.add_context(f"The tool failed with this error: {str(e)}. I need to inform the user about this immediately before deciding what to do next. I need to tell the user the exact error with zero summarization.") 
            return {}


    @tool()
    async def fetch(self, dataset_id: str, agent: AgentRef, loop: LoopControllerRef, react_context: ReactContextRef) -> dict:
        """
        This tool fetches URLS for datasets.
        
        Args:
            dataset_id (str): The user's query to pass to the climate search tool.
        Returns:
            dict: ESGF fetch results
        """
        try:
            return self.esgf.tool_fetch(dataset_id)
        except Exception as e:
            self.add_context(f"The tool failed with this error: {str(e)}. I should inform the user immediately with the full text of the error.")
            return {}
        
    @tool()
    async def regrid_dataset(
        self,
        dataset: str,
        target_resolution: tuple,
        agent: AgentRef,
        loop: LoopControllerRef,
        aggregation: Optional[str] = "interp_or_mean",
    ) -> str:
        """
        This tool should be used to show the user code to regrid a netcdf dataset with detectable geo-resolution.

        If a user asks to regrid a dataset, use this tool to return them code to regrid the dataset.

        If you are given a netcdf dataset, use this tool instead of any other regridding tool.

        If you are asked about what is needed to regrid a dataset, please provide information about the arguments of this tool.

        Args:
            dataset (str): The name of the dataset instantiated in the jupyter notebook.
            target_resolution (tuple): The target resolution to regrid to, e.g. (0.5, 0.5). This is in degrees longitude and latitude.
            aggregation (Optional): The aggregation function to be used in the regridding. The options are as follows:
                'conserve'
                'min'
                'max'
                'mean'
                'median'
                'mode'
                'interp_or_mean'
                'nearest_or_mode'

        Returns:
            str: Status of whether or not the dataset has been persisted to the HMI server.
        """

        loop.set_state(loop.STOP_SUCCESS)
        code = agent.context.get_code(
            "flowcast_regridding",
            {
                "dataset": dataset,
                "target_resolution": target_resolution,
                "aggregation": aggregation,
            },
        )

        result = json.dumps(
            {
                "action": "code_cell",
                "language": "python3",
                "content": code.strip(),
            }
        )

        return result

    @tool()
    async def get_netcdf_plot(
        self,
        dataset_variable_name: str,
        agent: AgentRef,
        loop: LoopControllerRef,
        plot_variable_name: Optional[str] = None,
        lat_col: Optional[str] = "lat",
        lon_col: Optional[str] = "lon",
        time_slice_index: Optional[int] = 1,
    ) -> str:
        """
        This function should be used to get a plot of a netcdf dataset.

        This function should also be used to preview any netcdf dataset.

        If the user asks to plot or preview a dataset, use this tool to return plotting code to them.

        You should also ask if the user wants to specify the optional arguments by telling them what each argument does.

        Args:
            dataset_variable_name (str): The name of the dataset instantiated in the jupyter notebook.
            plot_variable_name (Optional): The name of the variable to plot. Defaults to None.
                If None is provided, the first variable in the dataset will be plotted.
            lat_col (Optional): The name of the latitude column. Defaults to 'lat'.
            lon_col (Optional): The name of the longitude column. Defaults to 'lon'.
            time_slice_index (Optional): The index of the time slice to visualize. Defaults to 1.

        Returns:
            str: The code used to plot the netcdf.
        """

        code = agent.context.get_code(
            "get_netcdf_plot",
            {
                "dataset": dataset_variable_name,
                "plot_variable_name": plot_variable_name,
                "lat_col": lat_col,
                "lon_col": lon_col,
                "time_slice_index": time_slice_index,
            },
        )

        result = await agent.context.evaluate(
            code,
            parent_header={},
        )

        output = result.get("return")

        return output
