import json
import requests
from config import API_KEY, BASE_URL, GROUP_ID

def fetch_stratification_details():
    """
    Fetch dynamic stratification details from the API.
    """
    url = f"{BASE_URL}/stratification-details"  # Replace with the correct endpoint for stratification details
    headers = {
        "Authorization": f"Apikey {API_KEY}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching stratification details: {response.status_code}")
        return None

def get_existing_boundaries():
    """
    Retrieve all existing boundaries.
    """
    url = f"{BASE_URL}/areas"
    headers = {
        "Authorization": f"Apikey {API_KEY}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

def reformat_geojson_feature(feature):
    """
    Reformats a single GeoJSON feature to the format expected by the SoilStack API.
    """
    field_name = feature["properties"].get("name", "Unnamed Field")

    formatted_data = {
        "name": field_name,
        "areas": [
            {
                "type": "Feature",
                "geometry": feature["geometry"],
                "properties": {
                    "name": field_name
                }
            }
        ]
    }
    return formatted_data

def process_geojson_file(file_path):
    """
    Loads the GeoJSON file and extracts its features.
    """
    try:
        with open(file_path, 'r') as file:
            geojson_data = json.load(file)
        return geojson_data.get("features", [])
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
        return []

def upload_geojson_field(formatted_data):
    """
    Uploads a single formatted GeoJSON feature to the SoilStack API.
    """
    url = f"{BASE_URL}/fields"
    headers = {
        "Authorization": f"Apikey {API_KEY}",
        "Content-Type": "application/json"
    }
    params = {
        "groupId": GROUP_ID
    }

    response = requests.post(url, headers=headers, params=params, json=formatted_data)
    
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error uploading field: {response.status_code} - {response.text}")
        return {"error": response.status_code, "message": response.text}

def get_field_id(field_name):
    """
    Retrieves the field ID by the field name.
    """
    boundaries = get_existing_boundaries()
    if "error" in boundaries:
        print(f"Error retrieving boundaries: {boundaries['message']}")
        return None

    for boundary in boundaries.get('areas', []):
        if boundary['properties']['name'] == field_name:
            return boundary['id']
    
    print(f"No field found with the name {field_name}")
    return None

def fetch_stratification_by_id(stratification_id):
    """
    Retrieves stratification details using the stratification ID.
    """
    url = f"{BASE_URL}/stratifications/{stratification_id}"
    headers = {
        "Authorization": f"Apikey {API_KEY}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching stratification: {response.status_code} - {response.text}")
        return None
