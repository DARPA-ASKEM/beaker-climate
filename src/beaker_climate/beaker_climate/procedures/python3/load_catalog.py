def __load():
    try:
        return pangeo_catalog.{{category}}.{{dataset}}
    except Exception as e: 
        return pangeo_catalog.{{category}}["{{dataset}}"]

{{dataset}} = __load()
