import requests
import json
from config import API_KEY, BASE_URL, GROUP_ID

def fetch_stratification_details():
    url = f"{BASE_URL}/stratification-details"  # Hypothetical endpoint for fetching stratification details
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
    url = f"{BASE_URL}/areas"
    headers = {
        "Authorization": f"Apikey {API_KEY}"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

def save_stratification(area_id, stratification_data):
    url = f"{BASE_URL}/areas/{area_id}/stratifications"
    headers = {
        "Authorization": f"Apikey {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, headers=headers, json=stratification_data)
    
    if response.status_code in [200, 201]:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

def process_geojson_file(file_path):
    with open(file_path, 'r') as file:
        geojson_data = json.load(file)
    return geojson_data['features']

def reformat_geojson_feature(feature):
    return {
        "type": "Feature",
        "geometry": feature["geometry"],
        "properties": {
            "name": feature["properties"]["name"]
        }
    }

def upload_geojson_field(formatted_data, group_id):
    url = f"{BASE_URL}/areas"
    headers = {
        "Authorization": f"Apikey {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "name": formatted_data["properties"]["name"],
        "areas": [formatted_data],
        "groupId": group_id
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code in [200, 201]:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}
