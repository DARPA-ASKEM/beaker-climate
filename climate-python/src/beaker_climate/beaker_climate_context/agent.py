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
        Provided below is the comprehensive documentation of the climate-search API that you have access to.
        ALWAYS reference this when using the climate-search API.                             
    ```
    {f.read()}
    ```
''')
                    initial_context_msg_added = True
                except Exception as e:
                    sleep(0.5)
       
    @tool()
    async def search_esgf(self, code: str, agent: AgentRef, loop: LoopControllerRef, react_context: ReactContextRef) -> str:
        """
        This tool should be used to write python code that makes a request to the climate-search API. 
        The base URL is http://climate:8000/.
        
        Be sure to import requests at the top of the code block.

        You will be using climate-search, a REST interface for ESGF operations like searching and downloading CMIP datasets.               
        This API interfaces with ESGF.
                       
        The Earth System Grid Federation (ESGF) is a global collaboration that manages and distributes climate and environmental science data. 
        It serves as the primary platform for accessing CMIP (Coupled Model Intercomparison Project) data and other climate model outputs.
        The federation provides a distributed database and delivery system for climate science data, particularly model outputs and observational data.
        Through ESGF, users can search, discover and access climate datasets from major modeling centers and research institutions worldwide.
        The system supports authentication, search capabilities, and data transfer protocols optimized for large scientific datasets.
        
        If you perform a search over datasets, be sure to 
        Pass the results of the search endpoint to the `summarize_search_metadata` tool afterward.

        If datasets are loaded, use xarray with the OpenDAP URL.
        If the user asks to download a dataset, ask them if they are sure they want to download it.

        Additionally, any data downloaded should be downloaded to the './data/' directory.
        Please ensure the code makes sure this location exists, and all downloaded data is saved to this location.

        Args:
            code (str): The python code to be ran that makes one or more climate-search API requests.
                        **You will be writing python code to make these requests.**
        Returns:
            str: A summary of the run, along with the collected stdout, stderr, returned result, display_data items, and any
                 errors that may have occurred.
        """
        try:
            result = await self.tools['run_code'](code, agent=agent, loop=loop, react_context=react_context)
            return result
        except Exception as e:
            self.logger.error(f"error in using ESGF client api: {e}")
            raise e

    @tool()
    async def summarize_search_metadata(self, results: str) -> str:
        '''
        You wil summarize the search metadata for the datasets and make a markdown-formatted summary of the metadata.

        Refer to the climate-search API documentation you understand if there are questions.

        The filesize in bytes of the dataset is in the `size` field of the metadata. Listing metadata attributes about datasets to the user is very useful. Convert sizes to human readable values such as MB or GB, as well as when asked to describe the dataset, mention coordinates, frequency, and resolution as important details.
        **If the user asks for information, mention filesize in human readable units, frequency, resolution, and variable. Summarize the metadata, DO NOT print it to the console.**

        Args:
            results (str): JSON returned from the search endpoint.
        Returns:
            str: markdown formatted summary of the metadata in human readable units
        '''
        return results

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
