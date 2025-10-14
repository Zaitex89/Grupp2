from typing import List, Dict
from omdb.omdb_client import OMDbClient
from ai.gpt_interpreter import GPTMovieInterpreter

class MovieRecommender:
    """Movie recommender that uses GPT for understanding user input."""
    
    def __init__(self):
        self.omdb = OMDbClient()
        self.ai = GPTMovieInterpreter()
    
    def get_recommendations(self, user_input: str, max_results: int = 5) -> List[Dict]:
        print("Thinking")
        interpretation = self.ai.interpret_request(user_input)
        print(f"AI Understanding: {interpretation.get('explanation', 'Processing...')}")
        print(f"Searching for: {', '.join(interpretation.get('search_terms', []))}")
        all_movies = []
        seen_ids = set()
        
        for search_term in interpretation.get('search_terms', []):
            movies = self.omdb.search_movies(search_term)
            
            for movie in movies:
                movie_id = movie.get('imdbID')
                if movie_id and movie_id not in seen_ids:
                    details = self.omdb.get_movie_details(imdb_id=movie_id)
                    if details:
                        all_movies.append(details)
                        seen_ids.add(movie_id)
        
        if all_movies:
            print(f"Found {len(all_movies)} movies. Using AI to rank them...")
            all_movies = self.ai.get_better_recommendations(all_movies, user_input)
            
            # Add AI commentary to top results
            print("Generating AI commentary...")
            for movie in all_movies[:max_results]:
                movie['ai_commentary'] = self.ai.generate_movie_commentary(movie, user_input)
        
        return all_movies[:max_results]
    
    def format_recommendation(self, movie: Dict) -> str:
        """Format movie for display."""
        output = []
        output.append(f"Title: {movie.get('Title', 'N/A')} ({movie.get('Year', 'N/A')})")
        output.append(f"IMDb Rating: {movie.get('imdbRating', 'N/A')}/10")
        output.append(f"Genre: {movie.get('Genre', 'N/A')}")
        output.append(f"Director: {movie.get('Director', 'N/A')}")
        
        plot = movie.get('Plot', 'N/A')
        if plot != 'N/A' and len(plot) > 200:
            plot = plot[:200] + '...'
        output.append(f"Plot: {plot}")
        
        if movie.get('gpt_score'):
            output.append(f"AI Match Score: {movie['gpt_score']}/5")
        
        # Add AI commentary here
        if movie.get('ai_commentary'):
            output.append(f"AI Commentary: {movie['ai_commentary']}")
        
        return '\n'.join(output)