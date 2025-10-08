from flask import Flask, render_template, request
from recommender.movie_recommender import MovieRecommender

app = Flask(__name__)
recommender = MovieRecommender()

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

    user_input = f"I like '{favorite_movie}', I'm feeling '{mood}'. {user_message}"
    ranked_movies = recommender.get_recommendations(user_input)

    return render_template('results.html', movies=ranked_movies)
    """
    # Skicka till AI
    prompt = (
        f"I'm in the mood for a movie. My current mood is '{mood}', "
        f"and I like '{favorite_movie}'. "
        f"Here's some extra context: '{user_message}'."
        f"Please recommend 3 movies with short explanations."
    )
    
    Här tänker jag att svar från AI kanske kan komma som en lista med dict {title: *, reason: *}

    ai_response = [
        {"title": "Inception", "reason": "You like mind-bending sci-fi."},
        {"title": "The Secret Life of Walter Mitty", "reason": "You're feeling adventurous."},
        {"title": "Her", "reason": "You enjoy emotional, futuristic stories."}
        ]
    
    ai_response = get_ai_recommendations(prompt)
    
    raw_movies = []
    for term in search_terms:
        results = omdb.search_movies(term)
        raw_movies.extend(results)

    detailed_movies = []
    for item in raw_movies:
        imdb_id = item.get("imdbID")
        details = omdb.get_movie_details(imdb_id=imdb_id)
        if details:
            detailed_movies.append(details)
    
    ranked_movies = gpt.get_better_recommendations(detailed_movies, user_input)
    """
