# climate-data 

On first context launch, caching data for search will be created - this may take around a minute. 

## Structure

The way this set of tools works follows a very specific workflow.
* Search for datasets with the `search` tool.
* Use the **dataset ID** and no other fields to pass to the `fetch` tool to download.
* Fetch will give URLs to download from; if you are downloading a dataset for the user, use the HTTP protocol set of URLs returned from the `fetch` tool.

Do not use the tools in other ways than this.

The `search` tool will return a JSON payload. Inside the response body, `"results"` is a list containing dataset metadata bundles. 

To fetch one of them, a list entry in `"results"` will have a `"metadata"` field containing an `"id"` field. **The `"id"` field is what should be passed to the `fetch` tool to download a file.

### CMIP6 (ESGF)

By default, climate-data will search all possible given mirrors for reliability - for endpoints, IDs with mirrors associated in the following form: (`CMIP6.CMIP.NCAR.CESM2.historical.r11i1p1f1.CFday.ua.gn.v20190514|esgf-data.ucar.edu`) should be considered **interchangeable** with mirrorless versions (`CMIP6.CMIP.NCAR.CESM2.historical.r11i1p1f1.CFday.ua.gn.v20190514`). Mirrorless versions should be considered the preferred form. 

#### Search Tool

Required Parameters:
* `query`: Natural language string with search terms to retrieve datasets for. 

Example: `/search/esgf?query=historical eastward wind 100 km cesm2 r11i1p1f1 cfday`

Output:  
```json
{
    "results": [
        {
            "metadata": {
                "id": "CMIP6.CMIP.NCAR.CESM2.historical.r11i1p1f1.CFday.ua.gn.v20190514|aims3.llnl.gov",
                "version": "20190514"...
            }
        }, ...
    ]
}
```

`results` is a list of datasets, sorted by relevance. 

Each dataset contains a `metadata` field. 

`metadata` contains all of the stored metadata for the data set, provided by ESGF, such as experiment name, title, variables, geospatial coordinates, time, frequency, resolution, and more. 

The filesize in bytes of the dataset is in the `size` field of the metadata. Listing metadata attributes about datasets to the user is very useful. Convert sizes to human readable values such as MB or GB, as well as when asked to describe the dataset, mention coordinates, frequency, and resolution as important details.

**If the user asks for information, mention filesize in human readable units, frequency, resolution, and variable. Summarize the metadata, DO NOT print it to stdout.**

The `metadata` field contains an `id` field that is used for subsequent processing and lookups, containing the full dataset ID with revision and node information, such as: `CMIP6.CMIP.NCAR.CESM2.historical.r11i1p1f1.CFday.ua.gn.v20190514|esgf-data.ucar.edu`

#### Fetch Tool

Required Parameters:
* `dataset_id`: ID of the dataset provided by search in full format. 

Example:  
`/fetch/esgf?dataset_id=CMIP6.CMIP.NCAR.CESM2.historical.r11i1p1f1.CFday.ua.gn.v20190514|esgf-data.ucar.edu`  

Output:
```json
{
    "dataset": "CMIP6.CMIP....",
    "urls": [
        {
            "http": [
                "http://esgf-data.node.example/http/part1...",
                "http://esgf-data.node.example/http/part2..."
            ],
            "opendap": [
                "http://esgf-data.node.example/opendap/part1...",
                "http://esgf-data.node.example/openda[/part2..."
            ]
        },
    ],
    "metadata": {}
}
```

The `urls` field returns a list of dicts mapping **protocol** to **a list of URLs** that comprise the download for each dataset. These files may be large, so they may be one singular download url or multipart, with multiple URLs. 

HTTP urls are provided for plain downloads.

OpenDAP supports `xarray.open_mfdataset()` for lazy network usage and disk usage. 
