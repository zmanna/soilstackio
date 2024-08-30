import requests
from config import API_KEY, BASE_URL

def get_all_stratifications():
    """
    Retrieves all stratifications.
    
    :return: The stratification data if successful, None otherwise.
    """
    # Construct the URL using the BASE_URL
    url = f"{BASE_URL}/stratifications"
    
    headers = {
        "Authorization": f"Apikey {API_KEY}"
    }
    
    # Make the GET request to retrieve stratifications
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the data if successful
    else:
        print(f"Error fetching stratifications: {response.status_code} - {response.text}")
        return None  # Return None if there was an error

def main():
    # Retrieve and display all stratifications
    stratifications = get_all_stratifications()
    
    if stratifications:
        print("Stratifications Data:")
        print(stratifications)
    else:
        print("No stratification data retrieved.")

if __name__ == "__main__":
    main()
