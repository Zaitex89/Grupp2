import sqlite3
import json

def init_db():
    with sqlite3.connect("history.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY,
                prompt TEXT NOT NULL,
                movies_json TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()

def save_to_history(user_input: str, movies: list[dict]):
    try:
        with sqlite3.connect("history.db") as connection:
            cursor = connection.cursor()
            movies_json = json.dumps(movies)
            cursor.execute(
                "INSERT INTO history (prompt, movies_json) VALUES (?, ?)",
                (user_input, movies_json)
            )
            connection.commit()
    except sqlite3.Error as e:
        print(f"Database error while saving history: {e}")

def get_last_10():
    try:
        with sqlite3.connect("history.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT prompt, movies_json, created_at
                FROM history
                ORDER BY id DESC
                LIMIT 10
            """)
            rows = cursor.fetchall()

        return [
            {
                "prompt": r[0],
                "movies": json.loads(r[1]),
                "created_at": r[2]
            }
            for r in rows
        ]

    except sqlite3.Error as e:
        print(f"Database error while fetching history: {e}")
        return []

