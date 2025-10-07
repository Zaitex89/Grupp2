import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recommender.movie_recommender import MovieRecommender

def main():
    """EVERYTHING STARTS HERE"""
    print("\n" + "="*60)
    print("AI MOVIE RECOMMENDER (Powered by GPT using shattered hopes and tears) ")
    print("="*60) # Line visuals because it's cool
    
    # Initialize the recommender
    try:
        print("\nInitializing AI system...")
        recommender = MovieRecommender()
        print("AI ready!")
    except ValueError as e:
        print(f"\nError: {e}")
        print("implement OMDB_API_KEY and OPENAI_API_KEY .env file")
        return
    
    print("\nTell me what kind of movies you want to watch!")
    print("I understand natural language, so just describe what you're looking for.")
    print("\nExamples:")
    print('  - "I want something mind-bending like Inception"')
    print('  - "Show me feel-good movies from the 90s"')
    print('  - "I need a good cry, something emotional"')
    print('  - "Action movies with great car chases"')
    print('  - "Something my kids would enjoy"') 
    print("Type 'quit' to exit\n") ## totally not gpt generated menu
    
    while True:
        try:
            # Get user input
            user_input = input("What kind of movies are you looking for? ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Thanks for using cybernet Movie Recommender. Goodbye!")
                break
            if not user_input:
                print("Please describe what kind of movies you'd like to watch.")
                continue
            # Get AI-powered recommendations
            recommendations = recommender.get_recommendations(user_input) # we call the function from the movie.recommender.py 
        
            if recommendations:
                print(f"\n{'='*60}")
                print(f"RECOMMENDATIONS (Ranked by AI)")
                print('='*60)
                
                for i, movie in enumerate(recommendations, 1):
                    print(f"\n{'---'} #{i} {'---'}")
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