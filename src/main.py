from src.api import upload_geojson_fields

def main():
    file_path = 'path_to_your_geojson_file.geojson'
    results = upload_geojson_fields(file_path)
    
    if results:
        print("All boundaries uploaded successfully!")
    else:
        print("Failed to upload some boundaries.")

if __name__ == "__main__":
    main()