import sys
import os
from dotenv import load_dotenv

# Load .env file
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(dotenv_path=env_path)

# Import your recommender and database functions
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recommender.movie_recommender import MovieRecommender
from featuressearched import init_db, save_to_history, get_last_10


def main():
    """EVERYTHING STARTS HERE"""
    print("\n" + "="*60)
    print("AI MOVIE RECOMMENDER (Powered by GPT using shattered hopes and tears)")
    print("="*60)

    # Initialize database // André 
    init_db()

    # Initialize the recommender
    try:
        print("Cybernet is active")
        recommender = MovieRecommender()
        print("Cybernet ready!")
    except ValueError as e:
        print(f"Error: {e}")
        return

    print("\nTell me what kind of movies you want to watch!")
    print("I understand natural language, so just describe what you're looking for.")
    print("\nExamples:")
    print('  - "I want something mind-bending like Inception"')
    print('  - "Show me feel-good movies from the 90s"')
    print('  - "I need a good cry, something emotional"')
    print('  - "Action movies with great car chases"')
    print('  - "Something my kids would enjoy"')
    print("Type 'history' to view your last 10 searches.") # wrote this //André
    print("Type 'quit' to exit.\n")

    while True:
        try:
            # Get user input
            user_input = input("What kind of movies are you looking for? ").strip()

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Thanks for using Cybernet Movie Recommender. Goodbye!")
                break

             
            if user_input.lower() == "history": #This part is mine //André
                last_searches = get_last_10()  # Fetches the 10 most recent searches from the database // André
            if not last_searches:
                print("\nNo previous searches found.")  # Informs user if no past searches exist // André
            else:
                print("\n" + "="*60)  # Prints a visual separator line
                print("PAST 10 SEARCHES")  # Prints section title
                print("="*60)  # Another separator line

                for idx, record in enumerate(last_searches, 1):  # Loops through each search record with numbering
                    print(f"\n[{idx}] {record['created_at']}")  # Shows search number and timestamp
                    print(f"Prompt: {record['prompt']}")  # Displays what the user searched for
                    print("Movies:")  # Header before listing movies

                    for movie in record['movies']:  # Loops through each movie in the search result
                        print(f"  - {movie.get('Title', 'Unknown')} ({movie.get('Year', 'N/A')})")  # Prints movie title and year

                print("\n" + "="*60)  # Prints a closing separator line for readability
            continue

            if not user_input:
                print("Please describe what kind of movies you'd like to watch.")
                continue

            # Get AI-powered recommendations
            recommendations = recommender.get_recommendations(user_input)

            # Save the search + results in the database // André
            save_to_history(user_input, recommendations)

            # Display recommendations
            if recommendations:
                print(f"\n{'='*60}")
                print("RECOMMENDATIONS (Ranked by AI)")
                print('='*60)
                for i, movie in enumerate(recommendations, 1):
                    print(f"\n--- #{i} ---")
                    print(recommender.format_recommendation(movie))
                print(f"\n{'='*60}")
                print("Want different recommendations? Just ask again with more details!")
            else:
                print("\nSorry, I couldn't find any movies matching your request.")
                print("Try describing what you want differently, or be more specific.")

        except KeyboardInterrupt:
            print("\n\nInterrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Something went wrong: {e}")
            print("Let's try again with a different request.")


if __name__ == '__main__':
    main()
