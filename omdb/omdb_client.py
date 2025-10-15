from abc import ABC, abstractmethod
import requests
from typing import Optional
import os
from dotenv import load_dotenv


class APIClient(ABC):
    """
    Abstract base class for different API clients.

    This class defines the basic structure for API clients that connect
    to web APIs. Other classes can inherit from this one to reuse
    common code such as API key handling and timeouts.
    """

    BASE_URL: str

    def __init__(self, api_key: str, timeout: int = 10):
        #Create a new API client.
        self._api_key = api_key
        self._timeout = timeout

    @abstractmethod
    def make_request(self, params: dict) -> dict:
        """
        Send a request to the API.

        This method must be implemented by all subclasses. It defines
        how an API call is made and how the response is handled.

        params (dict): The query parameters to include in the request.

        dict: The data returned from the API as a dictionary.
        """
        pass


class OMDbClient(APIClient):
    """
    Client for communicating with the OMDb (Open Movie Database) API.

    This class can search for movies and get detailed information
    about them using their title or IMDb ID.
    """

    BASE_URL = "http://www.omdbapi.com/"

    def __init__(self, api_key: Optional[str] = None, timeout: int = 10):
        """
        Set up the OMDb client and load the API key.

        The API key is read from a .env file unless it is given directly
        as a parameter.
        """
        load_dotenv()
        key = api_key or os.getenv("OMDB_API_KEY")
        if not key:
            raise ValueError("OMDB_API_KEY missing. Add it to .env file.")
        super().__init__(key, timeout)

    def make_request(self, params: dict) -> dict:
        """
        Send a request to the OMDb API.

        Args:
            params (dict): The parameters to send with the request.

        Returns:
            dict: The JSON response from the API as a dictionary.
                  Returns an empty dictionary if an error occurs.
        """
        params["apikey"] = self._api_key
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=self._timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API error: {e}")
            return {}

    def search_movies(
        self, 
        search_term: str, 
        media_type: str = "movie", 
        year: Optional[int] = None
    ) -> list[dict[str, str]]:
        """
        Search for movies using a word or title.

        Args:
            search_term (str): The title or keyword to search for.
            media_type (str, optional): Type of media to search for.
                                        Can be "movie", "series", or "episode".
                                        Default is "movie".
            year (int, optional): Limit results to a specific release year.

        Returns:
            list[dict[str, str]]: A list of movies that match the search.
                                  Each item includes the title, year, and IMDb ID.
        """
        params = {"s": search_term, "type": media_type}
        if year:
            params["y"] = str(year)
        data = self.make_request(params)
        if data.get("Response") == "True":
            return [{"Title": m["Title"], "Year": m["Year"], "imdbID": m["imdbID"]} 
                    for m in data.get("Search", [])]
        return []

    def get_movie_details(self, 
        imdb_id: Optional[str] = None, 
        title: Optional[str] = None, 
        full_plot: bool = True
    ) -> Optional[dict[str, str]]:
        """
        Get detailed information about a specific movie.

        You can look up a movie either by its IMDb ID or by its title.
        """
        if not imdb_id and not title:
            raise ValueError("You must provide either imdb_id or title.")
        params = {"plot": "full" if full_plot else "short"}
        if imdb_id:
            params["i"] = imdb_id
        elif title:
            params["t"] = title
        data = self.make_request(params)
        return data if data.get("Response") == "True" else None