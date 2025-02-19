"""
This script is used to generate a catalog of NOAA Physical Sciences Laboratory data from https://psl.noaa.gov/data/gridded/ and save it as a YAML file.
This data is comprised of thousands of NetCDF files, from one of 48 gridded weather datasets.
"""
import requests
import pandas as pd
import yaml
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
from tqdm import tqdm

def get_files_from_table(url, visited_urls=None, depth=0, max_depth=3):
    """Recursively get all .nc files and directories from a URL"""
    if visited_urls is None:
        visited_urls = set()
    
    if url in visited_urls or depth > max_depth:
        return {'files': [], 'directories': {}}
    
    print(f"{'  ' * depth}Checking URL: {url}")  # Debug print with indentation
    visited_urls.add(url)
    result = {'files': [], 'directories': {}}
    
    try:
        time.sleep(0.1)
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        if table:
            for row in table.find_all('tr'):
                links = row.find_all('a')
                for link in links:
                    href = link.get('href')
                    # Skip parent directory and empty links
                    if not href or href in ['../', '../', '/', '/Datasets/']:
                        continue
                    
                    # Get the base URL without query parameters
                    base_url = url.split('?')[0].rstrip('/')
                    full_url = f"{base_url}{href.lstrip('/')}"
                    if href.endswith('.nc'):
                        href = href.split('?dataset=')
                        if len(href) < 2:
                            print('failed to get opendap url')
                            continue
                        href = href[1]
                        access_url = f"https://psl.noaa.gov/thredds/dodsC/{href.lstrip('/')}"
                        print(f"{'  ' * depth}Found NC file: {href}")  # Debug print
                        # size_cell = row.find('td', class_='indexcolsize')
                        # modified_cell = row.find('td', class_='indexcollastmod')
                        
                        dataset_body = requests.get(full_url, timeout=10)
                        dataset_soup = BeautifulSoup(dataset_body.text, 'html.parser')
                        properties = dataset_soup.find('table', attrs='property-table')
                        if properties:
                            # size = dataset_soup.select_one('.context > tr:nth-child(2) > td:nth-child(2)')
                            # last_modified = dataset_soup.select_one('#dates > ul:nth-child(1) > li:nth-child(1)')
                            file_info = {
                                'url': access_url,
                                # 'size': size.text.strip() if size else None,
                                # 'last_modified': last_modified.text.split(': ')[1].strip() 
                                #     if last_modified else None
                            }
                            result['files'].append(file_info)
                        else:
                            print('failed to get properties from dataset')
                    elif href.endswith('/') and depth < max_depth:
                        print(f"{'  ' * depth}Found directory: {href}")  # Debug print
                        try:
                            dir_name = href.rstrip('/')
                            if full_url not in visited_urls:  # Extra check
                                dir_contents = get_files_from_table(full_url, visited_urls, depth + 1, max_depth)
                                if dir_contents.get('files') or dir_contents.get('directories'):
                                    result['directories'][dir_name] = dir_contents
                        except Exception as e:
                            print(f"{'  ' * depth}Error processing directory {full_url}: {e}")
                            continue
    
    except requests.RequestException as e:
        print(f"{'  ' * depth}Error accessing URL {url}: {e}")
    except Exception as e:
        print(f"{'  ' * depth}Unexpected error processing {url}: {e}")
    
    print(f"{'  ' * depth}Finished URL: {url}")  # Debug print
    return result

# Fetch the data from the API endpoint
api_url = "https://psl.noaa.gov/cgi-bin/mddb2/mddb2.py?action=getDatasets&category=0"
response = requests.get(api_url)
data = response.json()

# Create the dataset catalog
catalog = {}

# Add progress bar
for item in tqdm(data, desc="Processing datasets"):
    if item.get('path', "") == "":
        print("skipping pathless dataset")
    title = item.get('alt_title', "").strip()
    if title == "":
        title = item.get('title', '')
    print(title)
    description = item.get('desc', '').strip().replace('\r\n', '')
    download_link = f"https://psl.noaa.gov/thredds/catalog/{item['path'].lstrip('/')}/catalog.html" if item.get('path') else ''
    
    if download_link:
        print(f"\nProcessing dataset: {title}")
        catalog[title] = {
            'description': description,
            'public': item.get('public', False),
            'base_url': download_link,
            'contents': get_files_from_table(download_link)
        }

# Save as YAML
with open('noaa_catalog.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(catalog, f, sort_keys=True, allow_unicode=True, default_flow_style=False)

print("\nCatalog has been saved to noaa_catalog.yaml")
