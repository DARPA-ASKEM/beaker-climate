If you are asked to plot point data (e.g. military bases) or something like that you should use folium. You can use the following code to help inspire you:

```python
import folium
from folium.plugins import Fullscreen
import pandas as pd

def create_military_installations_map(df):
    """
    Create an interactive map of military installations using folium.
    
    Parameters:
    df : pandas DataFrame with columns 'baseLabel', 'lat', 'lon', 'typeLabel', 'countryLabel'
    
    Returns:
    folium.Map object
    """
    # Create a map centered on China with CartoDB Positron tiles
    m = folium.Map(location=[35, 105], 
                   zoom_start=4, 
                   tiles='CartoDB Positron',
                   control_scale=True)  # Add scale control

    # Add fullscreen button
    Fullscreen().add_to(m)

    # Define colors for different installation types
    installation_types = {
        'air base': 'red',
        'military base': 'blue',
        'naval base': 'darkblue',
        'military facility': 'purple',
        'military training area': 'orange',
        'fortress': 'darkred',
        'military academy': 'green'
    }

    # Add markers for each installation
    for idx, row in df.iterrows():
        # Skip if missing coordinates
        if pd.isna(row['lat']) or pd.isna(row['lon']):
            continue
            
        # Determine marker color based on installation type
        color = 'gray'  # default color
        for key in installation_types:
            if key.lower() in row['typeLabel'].lower():
                color = installation_types[key]
                break
        
        # Create popup content with HTML formatting
        popup_content = f"""
        <div style="font-family: Arial; width: 200px;">
            <h4 style="color: {color};">{row['baseLabel']}</h4>
            <b>Type:</b> {row['typeLabel']}<br>
            <b>Country:</b> {row['countryLabel']}<br>
            <b>Coordinates:</b> {row['lat']:.4f}, {row['lon']:.4f}
        </div>
        """
        
        # Add circle marker
        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            radius=6,  # Slightly smaller radius for better visibility when not clustered
            popup=folium.Popup(popup_content, max_width=300),
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            weight=2,
            opacity=0.8
        ).add_to(m)

    # Add a legend
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; right: 10px; width: 150px;
                border:2px solid grey; z-index:9999; font-size:12px;
                background-color:white;
                padding: 10px;
                opacity: 0.9;
                ">
                <h4 style="margin-top: 0; font-size: 13px;">Installation Types</h4>
                <div style="display: flex; align-items: center; margin: 3px;">
                    <div style="background-color: red; width: 12px; height: 12px; border-radius: 50%; margin-right: 5px;"></div>
                    <span>Air Base</span>
                </div>
                <div style="display: flex; align-items: center; margin: 3px;">
                    <div style="background-color: blue; width: 12px; height: 12px; border-radius: 50%; margin-right: 5px;"></div>
                    <span>Military Base</span>
                </div>
                <div style="display: flex; align-items: center; margin: 3px;">
                    <div style="background-color: darkblue; width: 12px; height: 12px; border-radius: 50%; margin-right: 5px;"></div>
                    <span>Naval Base</span>
                </div>
                <div style="display: flex; align-items: center; margin: 3px;">
                    <div style="background-color: purple; width: 12px; height: 12px; border-radius: 50%; margin-right: 5px;"></div>
                    <span>Military Facility</span>
                </div>
                <div style="display: flex; align-items: center; margin: 3px;">
                    <div style="background-color: orange; width: 12px; height: 12px; border-radius: 50%; margin-right: 5px;"></div>
                    <span>Training Area</span>
                </div>
                <div style="display: flex; align-items: center; margin: 3px;">
                    <div style="background-color: darkred; width: 12px; height: 12px; border-radius: 50%; margin-right: 5px;"></div>
                    <span>Fortress</span>
                </div>
                <div style="display: flex; align-items: center; margin: 3px;">
                    <div style="background-color: green; width: 12px; height: 12px; border-radius: 50%; margin-right: 5px;"></div>
                    <span>Military Academy</span>
                </div>
                <div style="display: flex; align-items: center; margin: 3px;">
                    <div style="background-color: gray; width: 12px; height: 12px; border-radius: 50%; margin-right: 5px;"></div>
                    <span>Other</span>
                </div>
    </div>
    '''

    m.get_root().html.add_child(folium.Element(legend_html))
    
    return m
```

Note the use of CartoDB Positron tiles for legibility as well as the inclusion of a full screen button.

If you are asked to fetch average max wind speed for some period of time, you should use code along the following lines:

```python
import xarray as xr
import numpy as np
import pandas as pd
import requests
from pathlib import Path
import os
from tqdm import tqdm
from datetime import datetime

def download_file(url, local_filename):
    """Download a file from a URL to a local file"""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)
    
    # Only download if file doesn't exist
    if not os.path.exists(local_filename):
        print(f"Downloading {url} to {local_filename}")
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        with open(local_filename, 'wb') as f:
            for chunk in tqdm(response.iter_content(chunk_size=8192), 
                            total=total_size//8192, unit='KB'):
                if chunk:
                    f.write(chunk)
    else:
        print(f"File {local_filename} already exists, skipping download")

def calculate_wind_speed(u, v):
    """Calculate wind speed from u and v components"""
    return np.sqrt(u**2 + v**2)

def find_nearest_point(lat, lon, lats, lons):
    """Find nearest grid point indices for given lat/lon"""
    lat_idx = np.abs(lats - lat).argmin()
    lon_idx = np.abs(lons - lon).argmin()
    return lat_idx, lon_idx

def analyze_wind_data(bases_file, wind_data_dir, year="2023"):
    """
    Analyze wind data for military bases
    
    Parameters:
    bases_file (str): Path to CSV file containing base locations
    wind_data_dir (str): Directory containing wind data files
    year (str): Year to analyze
    """
    try:
        # First, download the data if needed
        base_url = "https://downloads.psl.noaa.gov/Datasets/ncep.reanalysis/surface"
        uwnd_file = f"uwnd.sig995.{year}.nc"
        vwnd_file = f"vwnd.sig995.{year}.nc"
        
        # Local file paths
        local_uwnd = f"{wind_data_dir}/{uwnd_file}"
        local_vwnd = f"{wind_data_dir}/{vwnd_file}"
        
        # Download files
        download_file(f"{base_url}/{uwnd_file}", local_uwnd)
        download_file(f"{base_url}/{vwnd_file}", local_vwnd)
        
        print("\nFiles downloaded successfully. Now processing...")
        
        # Load the military bases data
        bases_df = pd.read_csv(bases_file)
        
        # Filter for air bases
        air_bases = bases_df[bases_df['typeLabel'].str.contains('air base', case=False, na=False)]
        print(f"Number of air bases found: {len(air_bases)}")
        
        # Load wind data from local files
        uwnd = xr.open_dataset(local_uwnd)
        vwnd = xr.open_dataset(local_vwnd)
        
        print("\nWind data loaded successfully")
        print("\nData dimensions:", uwnd.dims)
        print("\nTime range:", uwnd.time[0].values, "to", uwnd.time[-1].values)
        
        # Calculate maximum wind speed for each base location
        results = []
        
        for idx, base in air_bases.iterrows():
            # Find nearest grid point
            lat_idx, lon_idx = find_nearest_point(
                base['lat'], 
                base['lon'], 
                uwnd.lat.values, 
                uwnd.lon.values
            )
            
            # Extract wind components at this location
            u = uwnd.uwnd.isel(lat=lat_idx, lon=lon_idx)
            v = vwnd.vwnd.isel(lat=lat_idx, lon=lon_idx)
            
            # Calculate wind speed
            wind_speed = calculate_wind_speed(u, v)
            
            # Calculate statistics
            max_speed = float(wind_speed.max())
            mean_speed = float(wind_speed.mean())
            std_speed = float(wind_speed.std())
            
            # Calculate frequency of high-wind events (>10 m/s)
            high_wind_freq = (wind_speed > 10).mean().item() * 100  # percentage
            
            results.append({
                'base_name': base['baseLabel'],
                'latitude': base['lat'],
                'longitude': base['lon'],
                'max_wind_speed': max_speed,
                'mean_wind_speed': mean_speed,
                'std_wind_speed': std_speed,
                'high_wind_frequency': high_wind_freq
            })
        
        # Create DataFrame with results
        results_df = pd.DataFrame(results)
        
        # Display summary statistics
        print("\nWind Speed Statistics (m/s):")
        print("----------------------------")
        print(results_df[['max_wind_speed', 'mean_wind_speed', 
                         'std_wind_speed', 'high_wind_frequency']].describe())
        
        # Display top 5 bases with highest max wind speeds
        print("\nTop 5 Bases with Highest Maximum Wind Speeds:")
        print(results_df.nlargest(5, 'max_wind_speed')[
            ['base_name', 'max_wind_speed', 'mean_wind_speed', 'high_wind_frequency']
        ].to_string())
        
        # Save results to CSV
        output_file = f'wind_analysis_results_{year}.csv'
        results_df.to_csv(output_file, index=False)
        print(f"\nDetailed results saved to '{output_file}'")
        
        return results_df
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Configuration
BASES_FILE = "chinese_military_bases.csv"  # Your bases data file
WIND_DATA_DIR = "wind_data"  # Directory to store wind data
YEAR = "2023"  # Year to analyze

# Run the analysis
results = analyze_wind_data(BASES_FILE, WIND_DATA_DIR, YEAR)
```

If you are asked to plot this data with locations (e.g. bases) on a heat map you should use code along the following lines:

```python
import folium
from folium.plugins import Fullscreen
import xarray as xr
import numpy as np
import pandas as pd
import branca.colormap as cm
import json

def create_grid_geojson(lats, lons, wind_speed):
    """Create GeoJSON features for the wind speed grid"""
    features = []
    
    for i in range(len(lats)):
        for j in range(len(lons)):
            # Create a polygon feature for each grid cell
            polygon = {
                "type": "Feature",
                "properties": {
                    "speed": float(wind_speed[i, j])
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [float(lons[j] - 1.25), float(lats[i] - 1.25)],  # SW
                        [float(lons[j] + 1.25), float(lats[i] - 1.25)],  # SE
                        [float(lons[j] + 1.25), float(lats[i] + 1.25)],  # NE
                        [float(lons[j] - 1.25), float(lats[i] + 1.25)],  # NW
                        [float(lons[j] - 1.25), float(lats[i] - 1.25)]   # SW (close polygon)
                    ]]
                }
            }
            features.append(polygon)
    
    return {
        "type": "FeatureCollection",
        "features": features
    }

def create_military_wind_map(wind_data_dir, bases_file, output_file='military_installations_wind_map.html'):
    """
    Create an interactive map showing military installations and wind speeds
    
    Parameters:
    wind_data_dir (str): Directory containing wind data files
    bases_file (str): Path to CSV file containing military installation locations
    output_file (str): Name of output HTML file
    """
    try:
        # Load the wind data
        uwnd = xr.open_dataset(f'{wind_data_dir}/uwnd.sig995.2023.nc')
        vwnd = xr.open_dataset(f'{wind_data_dir}/vwnd.sig995.2023.nc')
        
        # Load the bases data
        bases_df = pd.read_csv(bases_file)
        
        print("Calculating wind speeds across the region...")
        
        # Get the lat/lon grids
        lats = uwnd.lat.values
        lons = uwnd.lon.values
        
        # Calculate mean wind speed for the year
        u_mean = uwnd.uwnd.mean(dim='time')
        v_mean = vwnd.vwnd.mean(dim='time')
        wind_speed = np.sqrt(u_mean**2 + v_mean**2)
        
        # Create the map
        m = folium.Map(location=[35, 105], 
                      zoom_start=4, 
                      tiles='CartoDB positron',
                      control_scale=True)
        
        # Add fullscreen button
        Fullscreen().add_to(m)
        
        # Create a custom colormap for wind speeds
        wind_colormap = cm.LinearColormap(
            colors=['blue', 'cyan', 'yellow', 'orange', 'red'],
            vmin=float(wind_speed.min()),
            vmax=float(wind_speed.max()),
            caption='Wind Speed (m/s)'
        )
        
        # Add the wind colormap to the map
        wind_colormap.add_to(m)
        
        # Create GeoJSON data
        print("Creating GeoJSON grid...")
        grid_geojson = create_grid_geojson(lats, lons, wind_speed)
        
        # Add GeoJSON layer
        print("Adding wind speed layer...")
        folium.GeoJson(
            grid_geojson,
            style_function=lambda feature: {
                'fillColor': wind_colormap.rgb_hex_str(feature['properties']['speed']),
                'color': 'none',
                'fillOpacity': 0.5,
            }
        ).add_to(m)
        
        # Define colors for different installation types
        installation_colors = {
            'air base': 'red',
            'military base': 'blue',
            'naval base': 'darkblue',
            'military facility': 'purple',
            'military training area': 'orange',
            'fortress': 'darkred',
            'military academy': 'green',
            'artillery battery': 'brown',
            'barracks': 'gray',
            'fire station': 'pink',
            'fort': 'black',
            'city gate': 'lightgray',
            'dzong in tibet': 'darkgreen',
            'military hospital': 'lightred',
            'castle': 'saddlebrown',
            'military area': 'cadetblue',
            'tulou': 'darkgoldenrod',
            'military university': 'darkslateblue',
            'Gompa': 'darkolivegreen',
            'fortified town': 'sienna',
            'defensive wall': 'dimgray',
            'Chinese city wall': 'tan',
            'watchtower': 'rosybrown',
            'military camp': 'olivedrab',
            'military medical university': 'mediumvioletred'
        }
        
        # Add markers for each military installation
        print("Adding installation markers...")
        for idx, base in bases_df.iterrows():
            # Find nearest point in wind speed grid
            lat_idx = np.abs(lats - base['lat']).argmin()
            lon_idx = np.abs(lons - base['lon']).argmin()
            local_wind_speed = float(wind_speed[lat_idx, lon_idx])
            
            # Determine marker color based on installation type
            base_type_lower = base['typeLabel'].lower()
            color = 'gray'  # default color
            for key in installation_colors:
                if key in base_type_lower:
                    color = installation_colors[key]
                    break
            
            # Create popup content
            popup_content = f"""
            <div style="font-family: Arial; width: 200px;">
                <h4 style="color: {color};">{base['baseLabel']}</h4>
                <b>Type:</b> {base['typeLabel']}<br>
                <b>Country:</b> {base['countryLabel']}<br>
                <b>Coordinates:</b> {base['lat']:.4f}, {base['lon']:.4f}<br>
                <b>Avg Wind Speed:</b> {local_wind_speed:.2f} m/s
            </div>
            """
            
            # Add circle marker
            folium.CircleMarker(
                location=[base['lat'], base['lon']],
                radius=6,
                popup=folium.Popup(popup_content, max_width=300),
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                weight=2,
                opacity=0.8
            ).add_to(m)
        
        # Add a legend for the markers
        legend_html = f'''
        <div style="position: fixed; 
                    bottom: 50px; right: 10px; width: 180px;
                    border:2px solid grey; z-index:9999; font-size:12px;
                    background-color:white;
                    padding: 10px;
                    opacity: 0.9;
                    max-height: 80vh;
                    overflow-y: auto;
                    ">
                    <h4 style="margin-top: 0; font-size: 13px;">Installation Types</h4>
        '''
        
        # Add an entry for each installation type
        for installation_type, color in installation_colors.items():
            legend_html += f'''
            <div style="display: flex; align-items: center; margin: 3px;">
                <div style="background-color: {color}; width: 12px; height: 12px; border-radius: 50%; margin-right: 5px;"></div>
                <span style="text-transform: capitalize;">{installation_type}</span>
            </div>
            '''
        
        legend_html += '</div>'
        
        m.get_root().html.add_child(folium.Element(legend_html))
        
        # Save the map
        m.save(output_file)
        print(f"\nMap saved as '{output_file}'")
        
        # Display some statistics
        print("\nInstallation Statistics:")
        print("------------------------")
        type_counts = bases_df['typeLabel'].value_counts()
        print(type_counts)
        
        return m
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Configuration
WIND_DATA_DIR = "wind_data"  # Directory containing wind data files
BASES_FILE = "chinese_military_bases.csv"  # File containing military installation data
OUTPUT_FILE = "military_installations_wind_map.html"  # Output map file

# Create the map
m = create_military_wind_map(WIND_DATA_DIR, BASES_FILE, OUTPUT_FILE)
m
```