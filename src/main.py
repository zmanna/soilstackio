from api import (
    get_existing_boundaries, 
    fetch_stratification_details, 
    process_geojson_file, 
    reformat_geojson_feature, 
    upload_geojson_field, 
    get_field_id, 
    fetch_stratification_by_id
)
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
        upload_result = upload_geojson_field(formatted_data)
        print(upload_result)

    # Example: Get field ID and use it to fetch a stratification
    field_name = "Your Field Name"  # Replace with actual field name
    field_id = get_field_id(field_name)
    
    if field_id:
        stratification_data = fetch_stratification_by_id(field_id)
        print(stratification_data)

if __name__ == "__main__":
    file_path = "Reid GeoJSON copy.geojson"  # Replace with your actual file path
    main(file_path)
