import requests


class OMDbClient:
    BASE_URL = "http://www.omdbapi.com/"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _make_request(self, params: dict):
        """Helper function to call the API and return JSON"""
        params["apikey"] = self.api_key
        response = requests.get(self.BASE_URL, params=params)
        return response.json()

    def get_movie_details(self, imdb_id: str):
        """Fetch full details for a movie by its IMDb ID"""
        return self._make_request({"i": imdb_id})

    def search_movies(self, keyword: str, page: int = 1):
        """Search for movies by keyword and print sorted results"""
        data = self._make_request({"s": keyword, "page": page})

        if data.get("Response") == "True":
            movies = data["Search"]

            def parse_year(movie):
                try:
                    return int(movie["Year"].split("–")[0])
                except ValueError:
                    return 0

            movies_sorted = sorted(movies, key=parse_year)

            print(f"\nMovies found for '{keyword}' (oldest first):\n")
            for idx, movie in enumerate(movies_sorted, start=1):
                details = self.get_movie_details(movie["imdbID"])
                imdb_rating = details.get("imdbRating", "N/A")
                print(f"{idx}. {movie['Title']} ({movie['Year']}) - IMDb: {imdb_rating}")
            print("\n")
        else:
            print("Error:", data.get("Error"))
