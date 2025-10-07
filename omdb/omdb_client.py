import os
import requests
from typing import Dict, List, Optional
from dotenv import load_dotenv

load_dotenv()

class OMDbClient:
    """Client for OMDb API communication."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('OMDB_API_KEY')
        if not self.api_key:
            raise ValueError("OMDB_API_KEY missing. Add it to .env file.")
        self.base_url = "http://www.omdbapi.com/"
    
    def search_movies(self, search_term: str) -> List[Dict]:
        """Search for movies based on search term."""
        params = {
            'apikey': self.api_key,
            's': search_term,
            'type': 'movie'
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get('Response') == 'True':
                return data.get('Search', [])
            return []
                
        except requests.exceptions.RequestException as e:
            print(f"API error: {e}")
            return []
    
    def get_movie_details(self, imdb_id: str = None, title: str = None) -> Optional[Dict]:
        """Get detailed information about a specific movie."""
        if not imdb_id and not title:
            return None
        
        params = {
            'apikey': self.api_key,
            'plot': 'full'
        }
        
        if imdb_id:
            params['i'] = imdb_id
        else:
            params['t'] = title
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get('Response') == 'True':
                return data
            return None
                
        except requests.exceptions.RequestException as e:
            print(f"API error: {e}")
            return None