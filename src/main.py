# main.py

from api import upload_all_geojson_fields

def main():
    """
    Main function to process and upload each GeoJSON feature.
    """
    file_path = "/Users/mannz/workspaces/holganix/soilStackio/Kaleb Dinwiddie.geojson"  # Replace with the actual path to your GeoJSON file
    
    results = upload_all_geojson_fields(file_path)
    print(results)

if __name__ == "__main__":
    main()
