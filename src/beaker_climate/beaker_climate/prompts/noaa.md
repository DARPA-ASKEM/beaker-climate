NOAA PSL contains thousands of NetCDF files, from one of 48 gridded weather datasets. The following is a catalog of datasets that 
are available for download, including dataset descriptions and links to the actual data files.

If the user asks you to load a dataset, you must download it first then load it (e.g. with xarray). While the URLs 
do allow direct downloading through a web browser, xarray cannot directly access it through HTTPS

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

Here is a list of datasets to load with NOAA.
Use the URL here.

```
'Air and Marine Temperature Anomalies: HadCRUT4':
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/cru/hadcrut4/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cru/hadcrut4/air.mon.anom.error.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cru/hadcrut4/air.mon.anom.median.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cru/hadcrut4/air.mon.ltm.nc
  description: Jones (CRU) Combined Air/Marine Temperature Anomalies
  public: 1
CMAP Precipitation:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/cmap//catalog.html
  contents:
    directories: {}
    files: []
  description: Monthly and pentad global gridded precipitation means. It includes
    a standard and enhanced version (with NCEP Reanalysis) from 1979 to near the present.
  public: 1
COBE Sea Surface Temperature:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/COBE/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/COBE/sst.mon.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/COBE/sst.mon.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/COBE/sst.mon.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/COBE/sst.mon.mean.nc
  description: Monthly 1Â° x1Â° SST dataset from 1891 to 2023 from the JMA. Datasets
    uses 3D Var to fill gaps.
  public: 1
COBE-SST 2 and Sea Ice:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/COBE2/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/COBE2/icec.mon.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/COBE2/icec.mon.mean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/COBE2/sst.mon.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/COBE2/sst.mon.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/COBE2/sst.mon.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/COBE2/sst.mon.mean.nc
  description: Monthly 1x1 SST dataset from 1850 from the Japanese Mateorolgical Center
    (JMA). It is the official SST monitoring dataset from the JMA.
  public: 1
CPC Daily Blended Outgoing Longwave Radiation (OLR) - 1 degree:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/cpc_blended_olr-1deg/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-1deg/olr.cbo-1deg.day.anom.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-1deg/olr.cbo-1deg.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-1deg/olr.cbo-1deg.day.mean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-1deg/olr.day.anom.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-1deg/olr.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-1deg/olr.day.mean.nc
  description: CBO V1 global OLR data set is constructed at NOAA Climate Prediction
    Center (CPC) by blending level 2 OLR retrievals from NASA Cloud and Earth RadiantEnergy
    (CERES) broadband measurements, NOAA/NESDIS Hyperspectral measurements, as well
    as High-resolution Infrared Radaition Sounder (HIRS)measurements.
  public: 1
CPC Daily Blended Outgoing Longwave Radiation (OLR) - 2.5 degree:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/cpc_blended_olr-2.5deg/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-2.5deg/olr.cbo-2.5deg.day.anom.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-2.5deg/olr.cbo-2.5deg.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-2.5deg/olr.cbo-2.5deg.day.mean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-2.5deg/olr.day.anom.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-2.5deg/olr.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-2.5deg/olr.day.mean.nc
  description: CBO V1 global OLR data set is constructed at NOAA Climate Prediction
    Center (CPC) by blending level 2 OLR retrievals from NASA Cloud and Earth Radiant
    Energy (CERES) broadband measurements, NOAA/NESDISHyperspectral measurements,
    as well as High-resolution Infrared Radaition Sounder (HIRS) measurements.
  public: 1
CPC Global Unified Gauge-Based Analysis of Daily Precipitation:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/cpc_global_precip/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.day.1981-2010.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.day.1991-2020.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.day.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.day.ltm.nc
  description: CPC 0.5x0.5 Global Daily Unified Gauge-Based Analysis of Precipitation.
  public: 1
CPC Global Unified Temperature:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/cpc_global_temp/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.day.1981-2010.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.day.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmax.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.day.1981-2010.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.day.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_temp/tmin.day.ltm.nc
  description: CPC 0.5x0.5 Global Daily Gridded Temperature
  public: 1
CPC Soil Moisture V2:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/cpcsoil/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/land.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/landmask.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/landperc.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/soilw.mon.1981-2010.ltm.v2.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/soilw.mon.1991-2020.ltm.v2.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/soilw.mon.ltm.1981-2010.v2.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/soilw.mon.ltm.1991-2020.v2.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/soilw.mon.ltm.v2.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/soilw.mon.mean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/soilw.mon.mean.v2.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/soilw.mon.v2.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpcsoil/soilw.mon.v2.ltm.1991-2020.nc
  description: Monthly Gridded CPC Soil Moisture from a model from 1948 to present.
  public: 1
CPC Unified Gauge-Based Analysis of Daily Precipitation over CONUS:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/cpc_us_precip/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/lsmask.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1948.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1949.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1950.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1951.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1952.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1953.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1954.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1955.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1956.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1957.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1958.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1959.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1960.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1961.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1962.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1963.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1964.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1965.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1966.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1967.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1968.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1969.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1970.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1971.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1972.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1973.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1974.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1975.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1976.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1977.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1978.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.day.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.mon.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.mon.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.mon.mean.nc
  description: 'CPC Unified Gauge-Based Analysis of Daily Precipitation over CONUS
    at PSD: Gridded Monthly Values. Monthly Values after 2006 are from the real time
    files (RT)'
  public: 1
CPC Unified Gauge-Based Analysis of Daily Precipitation over CONUS RT at PSD:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/cpc_us_precip/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/lsmask.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1948.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1949.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1950.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1951.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1952.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1953.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1954.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1955.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1956.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1957.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1958.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1959.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1960.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1961.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1962.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1963.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1964.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1965.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1966.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1967.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1968.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1969.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1970.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1971.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1972.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1973.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1974.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1975.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1976.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1977.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1978.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.day.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.mon.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.mon.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_us_precip/precip.V1.0.mon.mean.nc
  description: 'CPC Unified Gauge-Based Analysis of Daily Precipitation over CONUS
    at PSD: Gridded Monthly Values. Monthly Values after 2006 are from the real timefiles
    (RT)'
  public: 1
CRU Air Temperature and Combined Air Temperature/Marine Anomalies V4:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/cru/crutem4/catalog.html
  contents:
    directories: {}
    files: []
  description: Global gridded (5Â°x5Â°) monthly anomalies of observed air temperature
    and combined observed air and marine temperature (HADCRU4) from the mid1800's
    to near present.
  public: 1
GHCN Version 3 Land Temperature and Version 2 Land Precipitation Dataset:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/ghcngridded/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ghcngridded/air.mon.anom.v6.nc
  description: GHCN V3 contains gridded precipitation anomalies calculated from the
    GHCN version 2 monthly precipitation data set. 2,064 homogeneity adjustedprecipitation
    stations were combined with a data set containing 20,590 raw precipitation stations
    throughout the globe.
  public: 1
GHCN_CAMS Gridded 2m Temperature (Land):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/ghcncams/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ghcncams/air.mon.mean.nc
  description: GHCN CAMS is a high resolution (0.5x0.5) analyzed global land surface
    temperatures from 1948 to near present.
  public: 1
Global Precipitation Climatology Centre (GPCC):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/gpcc/catalog.html
  contents:
    directories: {}
    files: []
  description: GPCC Global Precipitation Climatology Centre monthly precipitation
    dataset from 1891-present is calculated from global station data.
  public: 1
Global Precipitation Climatology Project (GPCP) Monthly Analysis Product:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/gpcp/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/gpcp/precip.mon.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/gpcp/precip.mon.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/gpcp/precip.mon.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/gpcp/precip.mon.mean.error.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/gpcp/precip.mon.mean.nc
  description: The GPCP Monthly product provides a consistent analysis of global precipitation
    from an integration of various satellite data sets over land and ocean and a gauge
    analysis over land.
  public: 1
ICOADS:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/icoads/catalog.html
  contents:
    directories: {}
    files: []
  description: Global surface marine data from 1800 to near the present summarized
    in monthly gridded formats (2x2 degree boxes, or 1x1 degree boxes from 1960 forward),
    andoffering a variety of statistics.
  public: 1
Kaplan Extended SST V2:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/kaplan_sst/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/kaplan_sst/sst.mean.anom.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/kaplan_sst/sst.mon.anom.nc
  description: Gridded global SST anomalies from 1856-present derived from UK Met
    Office SST data which has had sophisticated statistical techniques applied to
    it to fill in gaps.
  public: 1
Livneh daily CONUS near-surface gridded meteorological and derived hydrometeorological data:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/livneh/catalog.html
  contents:
    directories: {}
    files: []
  description: This CONUS daily dataset from 1915 to 2011 is 1/16 resolution. The
    dataset variables have been generated using the <a href="https://www.hydro.washington.edu/Lettenmaier/Models/VIC/">Variable
    Infiltration Capacity <b>VIC</b> hydrologic model v.4.1.2.c</a> which was drivenwith
    the companion meteorological data.
  public: 1
NASA GISS Surface Temperature Analysis:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/gistemp/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/gistemp/landmask_2deg.nc
  description: Goddard Institute for Space Studies (GISS/NASA) surface temperature
    analysis for the globe; globally gridded at a 2x2 resolution.
  public: 1
NCEP Global Data Assimilation System GDAS:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/ncep/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/air.sfc.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/hgt.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/pr_wtr.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/rhum.sfc.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/slp.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfp.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/srfpt.day.ltm.1994.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpp.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/trpt.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/uwnd.sfc.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1979.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/ncep/vwnd.sfc.day.ltm.nc
  description: NCEP's twice-daily global analysis at 2.5Â° resolution on pressure
    levels which is a product of their operational forecast system.
  public: 1
NCEP Global Ocean Data Assimilation System (GODAS):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/godas/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obil.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dbss_obml.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/dzdt.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/pottmp.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/salt.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sltfl.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/sshg.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/thflx.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/ucur.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/uflx.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vcur.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1980.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/godas/vflx.2025.nc
  description: High Resolution Multi-level ocean analysis from NOAA/NCEP
  public: 1
NCEP North American Regional Reanalysis (NARR):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/NARR/catalog.html
  contents:
    directories: {}
    files: []
  description: NCEP's high resolution combined model and assimilated dataset. From
    1979 to near present 8-times daily, daily and monthly data is output on aNorthern
    Hemisphere Lambert Conformal Conic grid. See <strong><a href="/data/narr/">PSL's
    NARR project page</a></strong>.
  public: 1
NCEP-NCAR Reanalysis 1:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/ncep.reanalysis/catalog.html
  contents:
    directories: {}
    files: []
  description: NCEP/NCAR Reanalysis 1 consists of 4x daily, daily and monthly atmospheric
    model output from 1948 to near present. See <strong><a href="/data/reanalysis/reanalysis.shtml">PSL's
    NCEP R1 project page</a></strong>.
  public: 1
NCEP/DOE Reanalysis II:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/ncep.reanalysis2/catalog.html
  contents:
    directories: {}
    files: []
  description: NCEP-DOE Reanalysis 2 is an improved version of the NCEP Reanalysis
    I model that fixed errors and updated paramterizations of physical processes.
  public: 1
NH Ease-Grid Snow Cover:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/snowcover/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/snowcover/snowcover.mon.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/snowcover/snowcover.mon.mean.nc
  description: The NSIDC weekly snowcover and ice dataset has been interpolated to
    a 1Â° x 1Â° Northern Hemisphere grid and a monthly time-scale covering 1971 to1995.
  public: 1
NOAA Daily (non-interpolated) Outgoing Longwave Radiation (OLR):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/uninterp_OLR/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/uninterp_OLR/olr.daily.ltm.1979-1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/uninterp_OLR/olr.day.mean.nc
  description: Gridded OLR data from NCEP without interpolation. See the Interpolated
    OLR dataset for an interpolated version.
  public: 1
NOAA Extended Reconstructed SLP:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets.other/noaa.erslp/catalog.html
  contents:
    directories: {}
    files: []
  description: Extended Reconstruction of Historical Sea Level Pressure (SLP) Using
    improved statistical methods from 1854.
  public: 1
NOAA Extended Reconstructed SST V5:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/noaa.ersst.v5/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst.v5/sst.mnmean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst.v5/sst.mon.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst.v5/sst.mon.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst.v5/sst.mon.ltm.nc
  description: A global monthly SST analysis from 1854 to the present derived from
    ICOADS data with missing data filled in by statistical methods.
  public: 1
NOAA Extended Reconstructed Sea Surface Temperature (SST) V3b:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/noaa.ersst/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/err.mnmean.v3.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mnmean.v3.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mnmean.v4.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.1971-2000.ltm.v4.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.19712000.ltm.v3.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.1981-2010.ltm.v3.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.1981-2010.ltm.v4.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.v4.ltm.1971-2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.v4.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.v4.ltm.nc
  description: A global monthly SST analysis from 1854 to 2020 derived from ICOADS
    data with missing data filled in by statistical methods.
  public: 1
NOAA Extended Reconstructed Sea Surface Temperature (SST) V4:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/noaa.ersst/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/err.mnmean.v3.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mnmean.v3.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mnmean.v4.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.1971-2000.ltm.v4.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.19712000.ltm.v3.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.1981-2010.ltm.v3.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.1981-2010.ltm.v4.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.v4.ltm.1971-2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.v4.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst/sst.mon.v4.ltm.nc
  description: A global monthly SST analysis from 1854 to 2020 derived from ICOADS
    data with missing data filled in by statistical methods.
  public: 1
NOAA Global Surface Temperature (NOAAGlobalTemp):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/noaaglobaltemp/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaaglobaltemp/air.mon.anom.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaaglobaltemp/air.mon.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaaglobaltemp/lsmask.nc
  description: Monthly gridded anomalies of air temperature blended from different
    dataset sources.
  public: 1
NOAA Highly Reflective Clouds:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/noaa_hrc/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa_hrc/hrc.dailies.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa_hrc/hrc.ltmstddev.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa_hrc/hrc.monthlies.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa_hrc/hrc.nmissdays.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa_hrc/hrc.norm_monthlies.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa_hrc/hrc.normltm.nc
  description: NOAA Highly Reflective Cloud Observations for the Global Tropics
  public: 1
NOAA Interpolated Outgoing Longwave Radiation (OLR):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/interp_OLR/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/interp_OLR/olr.2xdaily.1979-2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/interp_OLR/olr.day.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/interp_OLR/olr.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/interp_OLR/olr.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/interp_OLR/olr.day.mean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/interp_OLR/olr.mon.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/interp_OLR/olr.mon.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/interp_OLR/olr.mon.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/interp_OLR/olr.mon.mean.1975.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/interp_OLR/olr.mon.mean.nc
  description: Gridded daily and monthly OLR data from NCAR with temporal interpolation.
  public: 1
NOAA OI SST V2 High Resolution Dataset:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/noaa.oisst.v2.highres/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.day.mean.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.mon.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.mon.mean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/icec.week.mean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/lsmask.oisst.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.anom.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.err.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1981.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1983.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1984.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1985.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1986.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1987.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1988.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1991.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1992.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1993.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1994.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1995.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1996.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1997.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1998.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.1999.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2001.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2002.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2003.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2004.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2005.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2006.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2007.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2008.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2009.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2011.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2012.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2013.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2014.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2015.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2016.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2017.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2018.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2019.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2021.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2022.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2023.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2024.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2025.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.ltm.1971-2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.ltm.1982-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.mon.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.week.mean.nc
  description: NOAA High-resolution Blended Analysis of Daily SST and Ice. Data is
    from Sep 1981 and is on a 1/4 Â° global grid.
  public: 1
NOAA Optimum Interpolation (OI) SST V2:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/noaa.oisst.v2/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/err.wkmean.1981-1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/err.wkmean.1990-present.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/icec.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/icec.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/icec.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/icec.mnmean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/icec.wkmean.1981-1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/icec.wkmean.1990-present.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/lsmask.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.ltm.1961-1990.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.ltm.1971-2000.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.mnmean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.oisst.mon.mean.1982.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.wkmean.1981-1989.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.wkmean.1990-present.nc
  description: NOAA Optimum Interpolation (OI) Sea Surface Temperature (SST) V2
  public: 1
'NOAA''s Outgoing Longwave Radiation - Daily Climate Data Record (OLR -  Daily CDR): PSL Interpolated Version':
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/olrcdr/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/olrcdr/olr.day.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/olrcdr/olr.day.ltm.1991-2020.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/olrcdr/olr.day.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/olrcdr/olr.day.mean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/olrcdr/olr.mon.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/olrcdr/olr.mon.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/olrcdr/olr.mon.mean.nc
  description: Gridded daily 1x1 OLR CDR data from NCDC interpolated to -90 to 90.
  public: 1
NOAA's Precipitation Reconstruction (PREC):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/prec/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/prec/precip.mon.1991-2020.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/prec/precip.mon.anom.nc
  description: NOAA's Gridded Precipitation Reconstruction (PREC)
  public: 1
NOAA's Precipitation Reconstruction over Land (PREC/L):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/precl/catalog.html
  contents:
    directories: {}
    files: []
  description: NOAA's Gridded Precipitation Reconstruction over Land (PREC/L)
  public: 1
NOAA-CIRES 20th Century Reanalysis (V2):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/20thC_ReanV2/catalog.html
  contents:
    directories: {}
    files: []
  description: A long (1871-2012) 3-D atmospheric reanalyses that is output 4-8 time
    daily with multiple variables on both pressure land single levels.<strong><a href="/data/20thC_Rean/">PSL's
    20CR project page</a></strong> has more details.
  public: 1
NOAA-CIRES 20th Century Reanalysis (V2c):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/20thC_ReanV2c/catalog.html
  contents:
    directories: {}
    files: []
  description: NOAA-CIRES 20th Century Reanalysis V2c contains objectively-analyzed
    4-dimensional weather maps and their uncertainty from the mid 19th century to21st
    century. <strong><a href="/data/20thC_Rean/">PSL's 20CR project page</a></strong>
    has more details
  public: 1
NOAA/CIRES/DOE 20th Century Reanalysis (V3):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/20thC_ReanV3/catalog.html
  contents:
    directories: {}
    files: []
  description: NOAA-CIRES-DOE 20th Century Reanalysis V3 contains objectively-analyzed
    4-dimensional weather maps and their uncertainty from the early 19th centuryto
    the 21st century. (<a href="/data/20thC_Rean/">20CR Project</a>).
  public: 1
NODC (Levitus) World Ocean Atlas 1994:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/nodc.woa94/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/chi.mon.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/mldpd.mnltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/mldpt.mnltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/otemp.hr.annltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/otemp.hr.nobs.annltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/otemp.mnltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/otemp.nobs.mnltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/salt.hr.annltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/salt.hr.nobs.annltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/salt.mnltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/nodc.woa94/salt.nobs.mnltm.nc
  description: NODC (Levitus) World Ocean Atlas Data 1994
  public: 1
NODC World Ocean Atlas 1998:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/nodc.woa98/catalog.html
  contents:
    directories: {}
    files: []
  description: NODC (Levitus) World Ocean Atlas Data 1998
  public: 1
Palmer Drought Severity Index (PDSI):
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/dai_pdsi/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/dai_pdsi/pdsi.mon.ltm.selfcalibrated.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/dai_pdsi/pdsi.mon.mean.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/dai_pdsi/pdsi.mon.mean.selfcalibrated.nc
  description: Monthly gridded global PDSI (Palmer Drought Severity Index) values
    from 1850-2014.
  public: 1
University of Delaware Terrestrial Precipitation:
  base_url: https://psl.noaa.gov/thredds/catalog/Datasets/udel.airt.precip/catalog.html
  contents:
    directories: {}
    files:
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/udel.airt.precip/air.mon.1981-2010.ltm.v501.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/udel.airt.precip/air.mon.ltm.v501.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/udel.airt.precip/air.mon.mean.v501.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/udel.airt.precip/air.mon.v501.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/udel.airt.precip/air.mon.v501.ltm.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/udel.airt.precip/precip.mon.1981-2010.ltm.v501.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/udel.airt.precip/precip.mon.ltm.v501.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/udel.airt.precip/precip.mon.total.v501.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/udel.airt.precip/precip.mon.v501.ltm.1981-2010.nc
    - url: https://psl.noaa.gov/thredds/dodsC/Datasets/udel.airt.precip/precip.mon.v501.ltm.nc
  description: Global gridded Monthly land precipitation and temperature.
  public: 1

```
