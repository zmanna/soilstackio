from api import get_existing_boundaries, save_stratification, process_geojson_file, reformat_geojson_feature, upload_geojson_field, GROUP_ID, fetch_stratification_details
from datetime import datetime

def main(file_path):
    # Fetch stratification details dynamically
    strat_details = fetch_stratification_details()
    if strat_details is None:
        print("Failed to fetch stratification details.")
        return

    agent_name = strat_details['agent_name']
    provider_name = strat_details['provider_name']
    algorithm_name = strat_details['algorithm_name']

    # Step 1: Process the GeoJSON file to extract features
    features = process_geojson_file(file_path)

    # Step 2: Reformat and upload each feature
    for feature in features:
        formatted_data = reformat_geojson_feature(feature)
        upload_result = upload_geojson_field(formatted_data, GROUP_ID)
        print(upload_result)

    # Step 3: Retrieve all existing boundaries after upload
    boundaries = get_existing_boundaries()

    if "error" in boundaries:
        print(f"Error retrieving boundaries: {boundaries['message']}")
        return

    # Step 4: Run stratification on each boundary
    for boundary in boundaries['areas']:
        area_id = boundary['id']
        coordinates = boundary['geometry']['coordinates'][0][0]  # Outer boundary coordinates
        longitude = coordinates[0]
        latitude = coordinates[1]
        
        stratification_data = {
            "name": f"Stratification for {boundary['properties']['name']}",
            "description": "Stratification based on predefined criteria",
            "agent": agent_name,
            "dateCreated": datetime.isoformat() + "Z",
            "provider": provider_name,
            "algorithm": algorithm_name,
            "locationCollection": {
                "type": "FeatureCollection",
                "features": [{
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [longitude, latitude]
                    },
                    "properties": {
                        "name": boundary['properties']['name']
                    }
                }]
            }
        }
        
        result = save_stratification(area_id, stratification_data)
        print(result)

if __name__ == "__main__":
    file_path = "Reid GeoJSON copy.geojson"
    main(file_path)