import os
from dotenv import load_dotenv

# Construct the full path to the .env file
dotenv_path = '/Users/mannz/workspaces/holganix/soilStackio/env/soilstackio.env'

# Load environment variables from the .env file
load_dotenv(dotenv_path=dotenv_path)

# Check if the .env file is loaded correctly
print(f"Loading .env from: {dotenv_path}")

# Retrieve environment variables
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
GROUP_ID = os.getenv('GROUP_ID')

# Print the retrieved values for debugging

'''print(f"API_KEY: {API_KEY}, BASE_URL: {BASE_URL}, GROUP_ID: {GROUP_ID}")

# Check if any variables are missing
missing_vars = []
if not API_KEY:
    missing_vars.append('API_KEY')
if not BASE_URL:
    missing_vars.append('BASE_URL')
if not GROUP_ID:
    missing_vars.append('GROUP_ID')

if missing_vars:
    print(f"Missing environment variables: {', '.join(missing_vars)}")
    raise ValueError("One or more environment variables are missing.")
'''