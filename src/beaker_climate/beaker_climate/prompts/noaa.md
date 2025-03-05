NOAA PSL contains thousands of NetCDF files, from one of 48 gridded weather datasets. The following is a catalog of datasets that 
are available for download, including dataset descriptions and links to the actual data files.

If the user asks you to load a dataset, you can load it with xarray.
So you'll need to do something like:

```python
import requests
import xarray as xr
import os

# URL of the dataset
url = 'https://psl.noaa.gov/thredds/dodsC/Datasets/cru/hadcrut4/air.mon.anom.median.nc'

# Now load the local file with xarray
print("\nLoading the dataset with xarray...")
ds = xr.open_dataset(url)

# Display basic information about the dataset
print("\nDataset Information:")
print("-------------------")
print(ds.info())

# Display the first few time steps of data
print("\nFirst few time steps of temperature anomalies:")
print("--------------------------------------------")
print(ds['air'].isel(time=slice(0, 3)))
```

Use the consult_api_tool to see what's available with NOAA's datasets.
