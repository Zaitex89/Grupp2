import os
import requests
from typing import Dict, List, Optional
from dotenv import load_dotenv

load_dotenv()

class OMDbClient:
    """
    Client for communicating with the OMDb API.

    This class allows you to search for movies and get detailed information
    about specific titles using their IMDb ID or movie name.
    """

    BASE_URL: str = "http://www.omdbapi.com/"

    def __init__(self, api_key: Optional[str] = None, timeout: int = 10):
        """
        Initialize the OMDb client.

        Args:
            api_key (str, optional): Your OMDb API key. If not provided,
                it will be read from the .env file as 'OMDB_API_KEY'.
            timeout (int): Timeout in seconds for API requests (default is 10).

        Raises:
            ValueError: If no API key is provided or found in the environment.
        """
        
        api_key_from_env: Optional[str] = api_key or os.getenv("OMDB_API_KEY")
        if api_key_from_env is None:
            raise ValueError("OMDB_API_KEY missing. Add it to .env file.")
        self.api_key: str = api_key_from_env  # Now guaranteed to be str
        self.timeout: int = timeout

    def search_movies(
        self,
        search_term: str,
        media_type: str = "movie",
        year: Optional[int] = None
    ) -> list[dict[str, str]]:
        """
        Search for movies by a given search term.

        Args:
            search_term (str): The title or keyword to search for.
            media_type (str): Type of media to search (movie, series, or episode).
            year (int, optional): Optional release year to narrow results.

        Returns:
            list[dict]: A list of movies matching the search, each containing
            basic info like Title, Year, and IMDb ID.
        """
        params= {
            "apikey": self.api_key,
            "s": search_term,
            "type": media_type
        }
        if year is not None:
            params["y"] = str(year)

        try:
            response: requests.Response = requests.get(
                self.BASE_URL, params=params, timeout=self.timeout
            )
            response.raise_for_status()
            data: dict = response.json()

            if data.get("Response") == "True":
                # Return only essential fields
                return [
                    {"Title": m["Title"], "Year": m["Year"], "imdbID": m["imdbID"]}
                    for m in data.get("Search", [])
                ]
            return []

        except requests.exceptions.RequestException as e:
            print(f"API error: {e}")
            return []

    def get_movie_details(
        self,
        imdb_id: Optional[str] = None,
        title: Optional[str] = None,
        full_plot: bool = True
    ) -> Optional[dict[str, str]]:
        """
        Get detailed information about a specific movie.

        Args:
            imdb_id (str, optional): IMDb ID of the movie (e.g. "tt1375666").
            title (str, optional): Movie title if IMDb ID is not provided.
            full_plot (bool): Whether to return the full or short plot description.

        Returns:
            dict or None: Movie details if found, otherwise None.

        Raises:
            ValueError: If neither IMDb ID nor title is provided.
        """
        if imdb_id is None and title is None:
            raise ValueError("You must provide either imdb_id or title.")

        params: dict[str, str] = {
            "apikey": self.api_key,
            "plot": "full" if full_plot else "short"
        }

        # Only assign if the value is str, satisfies type checker
        if imdb_id is not None:
            params["i"] = imdb_id
        elif title is not None:
            params["t"] = title

        try:
            response: requests.Response = requests.get(
                self.BASE_URL, params=params, timeout=self.timeout
            )
            response.raise_for_status()
            data: dict = response.json()

            if data.get("Response") == "True":
                return data
            return None

        except requests.exceptions.RequestException as e:
            print(f"API error: {e}")
            return None
