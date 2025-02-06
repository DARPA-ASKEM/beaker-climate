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
        self.catalog = CMIP6Catalog()
        self.last_search : pandas.DataFrame
        super().__init__(context, tools, **kwargs)

    @tool()
    def search(
        self, 
        free_text: Optional[str],
        keywords: dict[str, str],
        agent: AgentRef, 
        loop: LoopControllerRef, 
        react_context: ReactContextRef
    ):
        """
        Search the catalog using keywords and/or specific parameters.
        Prefer using free_text if the keyword attribute is not known for the user's request.
        Fills the last search state.
        
        Example:
        --------
            >>> results = search(keywords='temperature', variable_id='tas')
            >>> results = search(experiment_id='historical', table_id='Amon')

        Args:
            free_text (str | None): Free-text search across all fields
            keywords (dict): Specific search parameter attributes (e.g., variable_id='tas', experiment_id='historical')
                                Valid keys include: 'activity_id', 'experiment_id', 'variable_id', 
                                'source_id', 'table_id', 'grid_label'            
        """
        self.last_search = self.catalog.search(keywords=free_text, *keywords)

    @tool
    def get_available_values_for_attribute(self, attribute: str) -> list[str]:
        """
        Get available values for a specific attribute.
        
        Args:
            attribute (str): The attribute to get values for (e.g., 'activity_id', 'variable_id')
            
        Returns:
            List[str]: List of available values for the attribute
        """
        try: 
            return self.catalog.get_available_values(attribute)
        except ValueError:
            return [f"Invalid attribute. Choose from: {list(self.catalog.unique_values.keys())}"]
    
    @tool
    def get_dataset(self,
                    target_variable: str,
                    source_id: Optional[str] = None,
                    member_id: Optional[str] = None,
                    chunks: Optional[dict] = None,
                    ):
        """
        Get an xarray dataset from search results with improved cloud access.
        Requires there to be a search beforehand.

        Example:
        --------
            >>> results = search(variable_id='tas', experiment_id='historical')
            >>> ds = get_dataset(results, source_id='IPSL-CM6A-LR', member_id='r1i1p1f1')
            >>> # With preprocessing
            >>> def preprocess(ds):
            ...     ds['tas'] = ds['tas'] - 273.15  # Convert to Celsius
            ...     return ds
            >>> ds = get_dataset(results, source_id='IPSL-CM6A-LR', preprocess=preprocess)


        Args:
            target_variable (str): Notebook variable to save the dataset to
            source_id (str | None): Specific model to load (e.g., 'IPSL-CM6A-LR')
            member_id (str | None): Specific ensemble member to load (e.g., 'r1i1p1f1')
            chunks (dict | None): Chunk sizes for dask arrays. Default is {'time': 100, 'lat': 45, 'lon': 45}
        """

        
        try:
            url = self.catalog.get_dataset_url(
                self.last_search, 
                source_id,
                member_id,
                chunks,
                preprocess=None)
            s_chunks = chunks if chunks is not None else r"{'time': 100, 'lat': 45, 'lon': 45}"
            code = f"""
chunk_dict = {s_chunks}
storage_options = {{
    'token': 'anon',  # For anonymous access
    'default_fill_cache': False,  # Avoid caching issues
    'default_cache_type': 'none'
}}
{target_variable} = xr.open_dataset(
    {url},
    engine='zarr',
    chunks=chunk_dict,
    backend_kwargs={{'storage_options': storage_options}},
    **kwargs
)
{target_variable}.attrs.update({
    'source_id': row['source_id'],
    'member_id': row['member_id'],
    'experiment_id': row['experiment_id'],
    'variable_id': row['variable_id'],
    'grid_label': row['grid_label']
})
            """
            self.tools['run_code'](code)
        except RuntimeError as e:
            self.add_context(f"Failed to load dataset: {e}")
            return ''
        
    @tool
    def summarize_results(self) -> dict:
        """
        Summarize search results with counts of models, experiments, etc.
        Requires a previous search.

        Returns:
            dict: Summary statistics of the search results
        """
        search_results = self.last_search
        summary = {
            'total_datasets': len(search_results),
            'unique_models': search_results['source_id'].nunique(),
            'unique_experiments': search_results['experiment_id'].nunique(),
            'models': search_results['source_id'].unique().tolist(),
            'experiments': search_results['experiment_id'].unique().tolist(),
            'variables': search_results['variable_id'].unique().tolist()
        }
        return summary

    @tool
    def get_model_details(self, model: str) -> dict:
        """
        Get detailed information about a specific model.
        
        Args:
            model (str): Model identifier (source_id)
        
        Returns:
            dict: Detailed information about the model
        """
        model_data = self.cat.df[self.cat.df['source_id'] == model]
        if len(model_data) == 0:
            raise ValueError(f"Model {model} not found in catalog")
        
        details = {
            'institution': model_data['institution_id'].iloc[0],
            'experiments': model_data['experiment_id'].unique().tolist(),
            'variables': model_data['variable_id'].unique().tolist(),
            'grid_labels': model_data['grid_label'].unique().tolist(),
            'ensemble_members': model_data['member_id'].unique().tolist(),
            'total_datasets': len(model_data)
        }
        return details
