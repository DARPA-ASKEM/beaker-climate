import intake
cat_url = 'https://raw.githubusercontent.com/pangeo-data/pangeo-datastore/master/intake-catalogs/master.yaml'
pangeo_catalog = intake.open_catalog(cat_url)
__pangeo_info = { 
    entry._name: {
        'description': entry._description,
        'metadata': entry._metadata,
        'category': category
    }
    for category in pangeo_catalog.keys()
    for _, entry in getattr(pangeo_catalog, category).walk(depth=5).items()
}

