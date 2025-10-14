import os
import json
from typing import List, Dict
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class GPTMovieInterpreter:
    """Uses OpenAI GPT to interpret user movie preferences."""
    
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY missing. Add it to .env file.")
        
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-3.5-turbo"  # or "gpt-4" if you have access
    
    def interpret_request(self, user_input: str) -> Dict:
        """Use GPT to interpret what the user wants."""
        
        prompt = f"""
        Analyze this movie request and extract search terms for the OMDb API.
        User request: "{user_input}"
        
        Return a JSON object with:
        - "search_terms": list of 3-5 specific movie titles or search keywords to use with OMDb API
        - "genres": list of genres the user might like
        - "mood": the mood/tone they want (action, thoughtful, funny, etc)
        - "explanation": brief explanation of what the user wants
        
        Example response:
        {{
            "search_terms": ["inception", "matrix", "interstellar"],
            "genres": ["sci-fi", "thriller"],
            "mood": "mind-bending",
            "explanation": "User wants complex sci-fi movies with twists"
        }}
        
        Focus on returning actual movie titles or very specific search terms that will work well with OMDb search.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a movie expert that helps find movies based on user preferences."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=200
            )
            
            # Parse GPT response
            content = response.choices[0].message.content
            if not content:
                content = "{}"  # Tom JSON som fallback

            
            # Try to parse as JSON
            try:
                result = json.loads(content)
            except json.JSONDecodeError:
                # If JSON parsing fails, extract what we can
                result = {
                    "search_terms": self._extract_basic_terms(user_input),
                    "genres": [],
                    "mood": "general",
                    "explanation": "Basic search based on keywords"
                }
            
            return result
            
        except Exception as e:
            print(f"GPT API error: {e}")
            # Fallback to basic extraction
            return {
                "search_terms": self._extract_basic_terms(user_input),
                "genres": [],
                "mood": "general",
                "explanation": "Fallback search due to API error"
            }
    
    def _extract_basic_terms(self, user_input: str) -> List[str]:
        """Basic fallback term extraction if GPT fails."""
        # Remove common words
        stop_words = {'i', 'want', 'like', 'movie', 'film', 'something', 'with', 'about', 'the', 'a', 'an'}
        words = user_input.lower().split()
        terms = [w for w in words if w not in stop_words and len(w) > 2]
        return terms[:3] if terms else ['popular']
    
    def generate_movie_commentary(self, movie: Dict, user_input: str) -> str:
        prompt = f"""
        User wants: "user_input"

        Movie: {movie.get('Title')} ({movie.get('Year')})
        Genre: {movie.get('Genre', 'N/A')}
        Original Plot: {movie.get('Plot', 'NA')}

        Write a brief, engaging 2-3 sentence explanation of why this movie matches what the user is looking for
        Be specific and enthusiastic. Don't just repeat the plot - explain the match. 
        """
        try:
            response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an enthusiastic movie recommender who explains why movies match user preferences."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )

            return response.choices[0].message.content.strip() if response.choices[0].message.content else movie.get('Plot', 'N/A')
        
        except Exception as e:
            print(f"Commentary generation error:{e}")
            return movie.get('Plot', 'N/A')



    def get_better_recommendations(self, movies: List[Dict], user_input: str) -> List[Dict]:
        """Use GPT to rank/filter movies based on user preference."""
        
        if not movies:
            return []
        
        # Prepare movie list for GPT
        movie_list = []
        for movie in movies[:10]:  # Limit to 10 to avoid token limits surely we wouldn't need a limiter
            movie_list.append({
                "title": movie.get('Title'),
                "year": movie.get('Year'),
                "genre": movie.get('Genre'),
                "plot": movie.get('Plot', '')[:100]  # First 100 chars of plot 
            })
        
        prompt = f"""
        User wants: "{user_input}"
        
        Here are some movies found. Rank them from 1-5 based on how well they match what the user wants.
        Return ONLY a JSON object with movie titles as keys and scores as values.
        
        Movies:
        {json.dumps(movie_list, indent=2)}
        
        Example response:
        {{"Inception": 5, "The Matrix": 4, "Tenet": 3, "Sharknado" 2}}
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a movie recommendation expert."}, # Brainwashing our little friend
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=150
            )
            
            content = response.choices[0].message.content or "{}"  # fallback to empty JSON
            try:
                scores = json.loads(content)
            except json.JSONDecodeError:
                scores = {}  # fallback if GPT returns invalid JSON
            
            # Add GPT scores to movies
            for movie in movies:
                title = movie.get('Title')
                if title in scores:
                    movie['gpt_score'] = scores[title]
                else:
                    movie['gpt_score'] = 0
            
            # Sort by GPT score
            movies.sort(key=lambda x: x.get('gpt_score', 0), reverse=True)
            
        except Exception as e:
            print(f"GPT ranking error: {e}")
        
        return movies