import os
from dotenv import load_dotenv

# Verify the file path
dotenv_path = '/Users/mannz/workspaces/holganix/soilStackio/env/soilstackio.env'
print(f"Loading .env file from: {dotenv_path}")

# Load environment variables
load_dotenv(dotenv_path=dotenv_path)

# Retrieve environment variables
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
GROUP_ID = os.getenv('GROUP_ID')
