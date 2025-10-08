import os
from dotenv import load_dotenv
from omdb import OMDbClient

# Load API key from .env
load_dotenv()
api_key = os.getenv("OMDB_API_KEY")

if not api_key:
    raise ValueError("No OMDB_API_KEY found in .env file!")

if __name__ == "__main__":
    client = OMDbClient(api_key)
    keyword = input("Enter keyword: ")
    client.search_movies(keyword)
