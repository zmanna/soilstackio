import requests
import json
from config import API_KEY, BASE_URL, GROUP_ID

def process_geojson_file(file_path):
    """Loads and processes the GeoJSON file, preparing it for the API."""
    with open(file_path, 'r') as file:
        geojson_data = json.load(file)
    return geojson_data['features']

def upload_boundary_to_soilstack(feature):
    """Uploads a single GeoJSON feature (boundary) to the SoilStack platform."""
    url = f"{BASE_URL}/fields"
    headers = {
        "Authorization": f"Apikey {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "name": feature['properties']['name'],
        "areas": [{
            "type": feature['type'],
            "geometry": feature['geometry'],
            "properties": {
                "name": feature['properties']['name']
            }
        }]
    }
    
    params = {
        "groupId": GROUP_ID
    }
    
    response = requests.post(url, headers=headers, params=params, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error uploading boundary: {response.status_code} - {response.text}")
        return None

def upload_geojson_fields(file_path):
    """Processes the GeoJSON file and uploads each boundary to SoilStack."""
    features = process_geojson_file(file_path)
    results = []
    
    for feature in features:
        result = upload_boundary_to_soilstack(feature)
        if result:
            results.append(result)
    
    return results
