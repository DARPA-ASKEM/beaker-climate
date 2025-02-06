import json
import logging
import re
from typing import Optional
import codecs

import pandas
import matplotlib.pyplot as plt
import xarray as xr

from typing import Callable
from archytas.react import Undefined
from archytas.tool_utils import AgentRef, LoopControllerRef, ReactContextRef, tool

from beaker_kernel.lib import BeakerAgent
from beaker_kernel.lib.context import BaseContext

from pathlib import Path
from .pangeo import CMIP6Catalog

logger = logging.getLogger(__name__)


class ClimateDataUtilityAgent(BeakerAgent):
    """
    You are assisting us in modifying geo-temporal datasets.

    The main things you are going to do are regridding spatial datasets, temporally rescaling datasets, and clipping the extent of geo-temporal datasets.

    If you don't have the details necessary to use a tool, you should use the ask_user tool to ask the user for them.
    """
    def __init__(self, context: BaseContext = None, tools: list = [], **kwargs):
        self.logger = logger
        super().__init__(context, tools, **kwargs)

    @tool()
    async def search(self, free_text: str, keywords: dict, agent: AgentRef) -> dict:
        """
        Search the catalog using keywords and/or specific parameters.
        Prefer using free_text if the keyword attribute is not known for the user's request.
        Fills the last search state.
        
        Args:
            free_text (Optional[str]): Free-text search across all fields
            keywords (Optional[dict]): Specific search parameter attributes (e.g., variable_id='tas', experiment_id='historical')
                                Valid keys include: 'activity_id', 'experiment_id', 'variable_id', 
                                'source_id', 'table_id', 'grid_label'            

        Returns:
            dict: a dictionary of search results (converted from a pandas dataframe)
        """
        code = agent.context.get_code("search", {"free_text": free_text, "keywords": keywords})
        response = await agent.context.evaluate(code)
        return response["return"]
    
    
    @tool()
    async def get_dataset(self, source_id: str, member_id: str, agent: AgentRef) -> str:
        """
        Get an xarray dataset from search results from pangeo (cmip6).

        Args:
            source_id (str): The source id of the dataset to get
            member_id (str): The member id of the dataset to get
        
        Returns:
            str: The dataset
        """
        code = agent.context.get_code("get_dataset", {"source_id": source_id, "member_id": member_id})
        response = await agent.context.evaluate(code)
        return response["return"]

    @tool
    async def get_available_values_for_attribute(self, attribute: str, agent: AgentRef) -> list[str]:
        """
        Get available values for a specific attribute.
        The attributes available to you are
        'source_id'
        'member_id'
        'experiment_id'
        'variable_id'
        'grid_label'
        'activity_id'
        'variable_id'
        
        Args:
            attribute (str): The attribute to get values for (e.g., 'activity_id', 'variable_id')
            
        Returns:
            List[str]: List of available values for the attribute
        """
        code = agent.context.get_code("get_attribute_values", {'attribute': attribute})
        response = await agent.context.evaluate(code)
        return response["return"]
        
#     @tool
#     def summarize_results(self) -> dict:
#         """
#         Summarize search results with counts of models, experiments, etc.
#         Requires a previous search.

#         Returns:
#             dict: Summary statistics of the search results
#         """
#         search_results = self.last_search
#         summary = {
#             'total_datasets': len(search_results),
#             'unique_models': search_results['source_id'].nunique(),
#             'unique_experiments': search_results['experiment_id'].nunique(),
#             'models': search_results['source_id'].unique().tolist(),
#             'experiments': search_results['experiment_id'].unique().tolist(),
#             'variables': search_results['variable_id'].unique().tolist()
#         }
#         return summary

#     @tool
#     def get_model_details(self, model: str) -> dict:
#         """
#         Get detailed information about a specific model.
        
#         Args:
#             model (str): Model identifier (source_id)
        
#         Returns:
#             dict: Detailed information about the model
#         """
#         model_data = self.cat.df[self.cat.df['source_id'] == model]
#         if len(model_data) == 0:
#             raise ValueError(f"Model {model} not found in catalog")
        
#         details = {
#             'institution': model_data['institution_id'].iloc[0],
#             'experiments': model_data['experiment_id'].unique().tolist(),
#             'variables': model_data['variable_id'].unique().tolist(),
#             'grid_labels': model_data['grid_label'].unique().tolist(),
#             'ensemble_members': model_data['member_id'].unique().tolist(),
#             'total_datasets': len(model_data)
#         }
#         return details
