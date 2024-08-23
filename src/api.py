import json
import requests
from config import API_KEY, BASE_URL, GROUP_ID

def reformat_geojson_feature(feature):
    """
    Reformats a single GeoJSON feature to the format expected by the SoilStack API.
    Includes required fields like name, areas, and other optional fields.
    """
    field_name = feature["properties"].get("name", "Unnamed Field")

    formatted_data = {
        "name": field_name,
        "areas": [
            {
                "type": "Feature",
                "geometry": feature["geometry"],
                "properties": {
                    "name": field_name,
                    "description": feature["properties"].get("description", ""),
                    "drawn": True  # Assuming the polygon was drawn
                }
            }
        ],
        "meta": {
            "referenceIds": [
                {
                    "owner": "surveystack",
                    "id": "some-id"  # Replace with actual ID if needed
                }
            ]
        }
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

def upload_all_geojson_fields(file_path):
    """
    Processes a GeoJSON file and uploads all features to the SoilStack API.
    """
    features = process_geojson_file(file_path)
    results = []
    
    for feature in features:
        formatted_data = reformat_geojson_feature(feature)
        result = upload_geojson_field(formatted_data)
        results.append(result)
    
    return results
