from flask import Flask, render_template, request
from omdb.omdb_client import OMDbClient
#from ai.ai_client import get_ai_recommendations
import os

app = Flask(__name__)
omdb = OMDbClient(api_key=os.getenv("OMDB_API_KEY"))

"""
1. Användaren fyller i formuläret
favorite_movie (eller genre)
mood

2. Flask skickar input till AI
exempel: Prompt: “I like [favorite_movie] and feel [mood].
Recommend 3 movies with short explanations.”
"""

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    favorite_movie = request.form.get('favorite_movie')
    mood = request.form.get('mood')
    user_message = request.form.get('user_message')

    # Skicka till AI
    prompt = (
        f"I'm in the mood for a movie. My current mood is '{mood}', "
        f"and I like '{favorite_movie}'. "
        f"Here's some extra context: '{user_message}'."
        f"Please recommend 3 movies with short explanations."
    )
    ai_response = get_ai_recommendations(prompt)

    """
    Här tänker jag att svar från AI kanske kan komma som en lista med dict {title: *, reason: *}

    [
    {"title": "Inception", "reason": "You like mind-bending sci-fi."},
    {"title": "The Secret Life of Walter Mitty", "reason": "You're feeling adventurous."},
    {"title": "Her", "reason": "You enjoy emotional, futuristic stories."}
    ]

    """

    enriched_movies = []
    for item in ai_response:
        title = item["title"] 
        reason = item["reason"]
        details = omdb.get_movie_by_title(title) 

        if details.get("Response") == "True":
            enriched_movies.append({
                "title": details.get("Title"),
                "year": details.get("Year"),
                "poster": details.get("Poster"),
                "rating": details.get("imdbRating"),
                "plot": details.get("Plot"),
                "genre": details.get("Genre"),
                "reason": reason,
                "imdb_link": f"https://www.imdb.com/title/{details.get('imdbID')}/"
            })
        else:
            # Hittas inte filmen, lägg till med ändå med AI:s info
            enriched_movies.append({
                "title": title,
                "year": "N/A",
                "poster": None,
                "rating": "N/A",
                "plot": "Not found in OMDb",
                "genre": "N/A",
                "reason": reason,
                "imdb_link": None

            })

    return render_template('results.html', movies=enriched_movies, mood=mood)