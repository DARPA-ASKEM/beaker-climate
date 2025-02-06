import intake
import xarray as xr
import pandas as pd
from typing import Dict, List, Union, Optional
import warnings
import fsspec

class CMIP6Catalog:
    """
    A class to handle CMIP6 data access through Pangeo's catalog.
    
    Available MIPs (Activities):
    - ScenarioMIP: Future scenario experiments
    - DCPP: Decadal prediction experiments
    - CMIP: Core experiments
    - PAMIP: Polar amplification experiments
    - DAMIP: Detection and attribution experiments
    - AerChemMIP: Aerosols and chemistry experiments
    - And others...
    
    Common Variables:
    - tas: near-surface air temperature
    - pr: precipitation
    - ps: surface pressure
    - tos: sea surface temperature
    - And many others...
    
    Example Usage:
    -------------
    >>> cat = CMIP6Catalog()
    >>> # Search for temperature data in historical experiments
    >>> results = cat.search(variable_id='tas', experiment_id='historical')
    >>> # Get dataset
    >>> ds = cat.get_dataset(results, model='IPSL-CM6A-LR')
    """
    
    def __init__(self, catalog_url: str = "https://storage.googleapis.com/cmip6/pangeo-cmip6.json"):
        """
        Initialize the CMIP6 catalog.
        
        Parameters:
        -----------
        catalog_url : str, optional
            URL to the Pangeo CMIP6 catalog
        """
        self.catalog_url = catalog_url
        self._load_catalog()
        
        # Configure default chunks for dask
        self.chunks = {'time': 100, 'lat': 45, 'lon': 45}
        
    def _load_catalog(self):
        """Load the catalog and store basic information."""
        try:
            self.cat = intake.open_esm_datastore(self.catalog_url)
            self._cache_unique_values()
        except Exception as e:
            raise ConnectionError(f"Failed to load catalog: {str(e)}")
            
    def _cache_unique_values(self):
        """Cache unique values for quick access to available options."""
        self.unique_values = {
            'activity_id': sorted(self.cat.df['activity_id'].unique()),
            'experiment_id': sorted(self.cat.df['experiment_id'].unique()),
            'variable_id': sorted(self.cat.df['variable_id'].unique()),
            'source_id': sorted(self.cat.df['source_id'].unique()),
            'table_id': sorted(self.cat.df['table_id'].unique()),
            'grid_label': sorted(self.cat.df['grid_label'].unique())
        }
        
    def get_available_values(self, attribute: str) -> List[str]:
        """
        Get available values for a specific attribute.
        
        Parameters:
        -----------
        attribute : str
            The attribute to get values for (e.g., 'activity_id', 'variable_id')
            
        Returns:
        --------
        List[str]
            List of available values for the attribute
        """
        if attribute not in self.unique_values:
            raise ValueError(f"Invalid attribute. Choose from: {list(self.unique_values.keys())}")
        return self.unique_values[attribute]

    def search(self, keywords: Optional[str] = None, **kwargs) -> pd.DataFrame:
        """
        Search the catalog using keywords and/or specific parameters.
        
        Parameters:
        -----------
        keywords : str, optional
            Free-text search across all fields
        **kwargs : dict
            Specific search parameters (e.g., variable_id='tas', experiment_id='historical')
            Valid keys include: 'activity_id', 'experiment_id', 'variable_id', 
            'source_id', 'table_id', 'grid_label'
        
        Returns:
        --------
        pd.DataFrame
            Filtered catalog entries matching the search criteria
        
        Example:
        --------
        >>> results = search(keywords='temperature', variable_id='tas')
        >>> results = search(experiment_id='historical', table_id='Amon')
        """
        # Start with the full catalog
        df = self.cat.df.copy()
        
        # Apply keyword search if provided
        if keywords:
            mask = pd.Series(False, index=df.index)
            for col in df.columns:
                if df[col].dtype == object:  # Only search string columns
                    mask |= df[col].astype(str).str.contains(keywords, case=False, na=False)
            df = df[mask]
        
        # Apply specific filters
        for key, value in kwargs.items():
            if key not in df.columns:
                warnings.warn(f"Invalid search key: {key}. Ignoring this parameter.")
                continue
            if isinstance(value, (list, tuple)):
                df = df[df[key].isin(value)]
            else:
                df = df[df[key] == value]
        
        return df

    def get_dataset(self, search_results: pd.DataFrame, 
                    source_id: Optional[str] = None,
                    member_id: Optional[str] = None,
                    chunks: Optional[Dict] = None,
                    preprocess: Optional[callable] = None,
                    **kwargs) -> xr.Dataset:
        """
        Get an xarray dataset from search results with improved cloud access.
        
        Parameters:
        -----------
        search_results : pd.DataFrame
            Results from the search method
        source_id : str, optional
            Specific model to load (e.g., 'IPSL-CM6A-LR')
        member_id : str, optional
            Specific ensemble member to load (e.g., 'r1i1p1f1')
        chunks : dict, optional
            Chunk sizes for dask arrays. Default is {'time': 100, 'lat': 45, 'lon': 45}
        preprocess : callable, optional
            Function to apply to dataset before returning
        **kwargs : dict
            Additional parameters passed to xarray.open_dataset()
        
        Returns:
        --------
        xr.Dataset
            The requested dataset
        
        Example:
        --------
        >>> results = search(variable_id='tas', experiment_id='historical')
        >>> ds = get_dataset(results, source_id='IPSL-CM6A-LR', member_id='r1i1p1f1')
        >>> # With preprocessing
        >>> def preprocess(ds):
        ...     ds['tas'] = ds['tas'] - 273.15  # Convert to Celsius
        ...     return ds
        >>> ds = get_dataset(results, source_id='IPSL-CM6A-LR', preprocess=preprocess)
        """
        # Make a copy to avoid modifying the original
        filtered_results = search_results.copy()
        
        # Filter by source_id (model) if specified
        if source_id:
            filtered_results = filtered_results[filtered_results['source_id'] == source_id]
        
        # Filter by member_id if specified
        if member_id:
            filtered_results = filtered_results[filtered_results['member_id'] == member_id]
        
        if len(filtered_results) == 0:
            raise ValueError("No datasets match the specified criteria")
        
        if len(filtered_results) > 1:
            available_models = filtered_results['source_id'].unique()
            available_members = filtered_results['member_id'].unique()
            warnings.warn(f"Multiple datasets found ({len(filtered_results)}).\n"
                        f"Available models: {available_models.tolist()}\n"
                        f"Available members: {available_members.tolist()}\n"
                        "Loading the first one.")
        
        # Get the first matching dataset
        row = filtered_results.iloc[0]
        
        try:
            # Set up cloud access options
            storage_options = {
                'token': 'anon',  # For anonymous access
                'default_fill_cache': False,  # Avoid caching issues
                'default_cache_type': 'none'
            }
            
            # Use the zstore URL if available, otherwise fall back to regular URL
            url = row.get('zstore', row.get('path'))
            if url is None:
                raise ValueError("No valid URL found in catalog entry")
            
            # Set up chunking
            chunk_dict = chunks if chunks is not None else self.chunks
            
            # Open the dataset with proper settings for cloud access
            ds = xr.open_dataset(
                url,
                engine='zarr',
                chunks=chunk_dict,
                backend_kwargs={'storage_options': storage_options},
                **kwargs
            )
            
            # Apply preprocessing if provided
            if preprocess is not None:
                ds = preprocess(ds)
            
            # Add metadata
            ds.attrs.update({
                'source_id': row['source_id'],
                'member_id': row['member_id'],
                'experiment_id': row['experiment_id'],
                'variable_id': row['variable_id'],
                'grid_label': row['grid_label']
            })
            
            return ds
            
        except Exception as e:
            raise RuntimeError(f"Failed to load dataset: {str(e)}\n"
                             f"URL attempted: {url}")

    def summarize_results(self, search_results: pd.DataFrame) -> Dict:
        """
        Summarize search results with counts of models, experiments, etc.
        
        Parameters:
        -----------
        search_results : pd.DataFrame
            Results from the search method
        
        Returns:
        --------
        Dict
            Summary statistics of the search results
        """
        summary = {
            'total_datasets': len(search_results),
            'unique_models': search_results['source_id'].nunique(),
            'unique_experiments': search_results['experiment_id'].nunique(),
            'models': search_results['source_id'].unique().tolist(),
            'experiments': search_results['experiment_id'].unique().tolist(),
            'variables': search_results['variable_id'].unique().tolist()
        }
        return summary

    def get_model_details(self, model: str) -> Dict:
        """
        Get detailed information about a specific model.
        
        Parameters:
        -----------
        model : str
            Model identifier (source_id)
        
        Returns:
        --------
        Dict
            Detailed information about the model
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

print("Setting up CMIP6Catalog")
catalog = CMIP6Catalog()
print("CMIP6Catalog setup complete")
catalog
