import os
import sqlite3

DATABASE_PATH_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database.db'))

def find(word: str):
    try:
        assert word.isalpha(), "You might be a Haput, else you could have entered a correct word."
        word = word.lower()

        conn = sqlite3.connect(DATABASE_PATH_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM data WHERE title = ?', (word.capitalize(),))
        result = cursor.fetchone()
        conn.commit()
        conn.close()

        if result:
            id, title, pos, englishMeaning, kashmiriMeaning, englishExample, kashmiriExample = result
            return {
                'title': title,
                'pos': pos,
                'englishMeaning': englishMeaning,
                'kashmiriMeaning': kashmiriMeaning,
                'englishExample': englishExample,
                'kashmiriExample': kashmiriExample
            }
        else:
            return "Not Found"
    except Exception as e:
        return (f"Error: {str(e)}")