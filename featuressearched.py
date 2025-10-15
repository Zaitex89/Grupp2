import sqlite3
import json

def init_db():
    # Creates (if not exists) a database called "history.db" with a table for storing search history
    with sqlite3.connect("history.db") as connection:  # Opens connection to the database
        cursor = connection.cursor()  # Creates a cursor to execute SQL commands
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY,  -- Unique ID for each search entry
                prompt TEXT NOT NULL,  -- The user’s search text
                movies_json TEXT NOT NULL,  -- The movies returned, stored as JSON text
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP  -- Timestamp when search was made
            )
        """)
        connection.commit()  # Saves (commits) the table creation


def save_to_history(user_input: str, movies: list[dict]):
    # Saves the user’s search prompt and movie results into the database
    try:
        with sqlite3.connect("history.db") as connection:  # Opens connection to the database
            cursor = connection.cursor()  # Creates a cursor for SQL operations
            movies_json = json.dumps(movies)  # Converts list of movies (Python dicts) into a JSON string
            cursor.execute(
                "INSERT INTO history (prompt, movies_json) VALUES (?, ?)",  # Inserts data into the table
                (user_input, movies_json)
            )
            connection.commit()  # Saves (commits) the new record into the database
    except sqlite3.Error as e:
        print(f"Database error while saving history: {e}")  # Prints an error message if something goes wrong


def get_last_10():
    # Retrieves the 10 most recent searches from the database
    try:
        with sqlite3.connect("history.db") as connection:  # Opens connection to the database
            cursor = connection.cursor()  # Creates a cursor for SQL operations
            cursor.execute("""
                SELECT prompt, movies_json, created_at  -- Selects the columns we need
                FROM history
                ORDER BY id DESC  -- Orders by latest entries first
                LIMIT 10  -- Only gets the last 10 searches
            """)
            rows = cursor.fetchall()  # Fetches all results into a list of tuples

        # Converts each tuple into a dictionary and loads the JSON movie data back into Python objects
        return [
            {
                "prompt": r[0],  # The search text
                "movies": json.loads(r[1]),  # The movie list (converted from JSON string back to dict)
                "created_at": r[2]  # The timestamp of when the search was made
            }
            for r in rows
        ]

    except sqlite3.Error as e:
        print(f"Database error while fetching history: {e}")  # Prints an error message if something goes wrong
        return []  # Returns an empty list if database query fails

