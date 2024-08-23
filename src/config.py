import os
from dotenv import load_dotenv

# Specify the path to your soilstackio.env file
dotenv_path = os.path.join(os.path.dirname(__file__), '../soilstackio.env')

# Load environment variables from the specified .env file
load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
GROUP_ID = os.getenv("GROUP_ID")
