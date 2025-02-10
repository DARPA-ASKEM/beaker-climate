try: 
    {{variable_name}} = __last_results['{{name}}'].to_dask()
except Exception as e:
    try:
        {{variable_name}} = """
            Failed to load dataset {{name}}. 
            Here were the last search results, consider loading one of these.
            
        """ + f"{__last_results}"
    except Exception as e:
        {{variable_name}} = "No search was performed before using this. Go and use the search tool."
{{variable_name}}
