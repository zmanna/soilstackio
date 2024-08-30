import requests
from config import API_KEY, GROUP_ID, BASE_URL

def get_all_stratifications(group_id=None):
    """
    Retrieves all stratifications, optionally filtering by groupId.
    
    :param group_id: Optional, the groupId to filter stratifications by.
    :return: The stratification data if successful, None otherwise.
    """
    # Construct the URL using the BASE_URL
    url = f"{BASE_URL}/stratifications"
    
    # If a groupId is provided, add it as a query parameter
    if group_id:
        url += f"?groupId={group_id}"
    
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
    stratifications = get_all_stratifications(GROUP_ID)
    
    if stratifications:
        print("Stratifications Data:")
        print(stratifications)
    else:
        print("No stratification data retrieved.")

if __name__ == "__main__":
    main()
