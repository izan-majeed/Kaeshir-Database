# from kashmiri.database import data
from database import data

import sqlite3

DEVELOPMENT = True

if DEVELOPMENT:
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Create a table to store your data
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        pos TEXT NOT NULL,
        englishMeaning TEXT NOT NULL,
        kashmiriMeaning TEXT NOT NULL,
        englishExample TEXT,
        kashmiriExample TEXT
    )
    ''')
    for item in data:
        cursor.execute('''
            INSERT INTO data (title, pos, englishMeaning, kashmiriMeaning, englishExample, kashmiriExample)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (item['title'], item['pos'], item['englishMeaning'], item['kashmiriMeaning'], item.get('englishExample'), item.get('kashmiriExample')))
    conn.commit()
    conn.close()

def find(word: str):
    assert word.isalpha(), "You might be a Haput, else you could have entered a correct word."
    word = word.lower()

    # Connect to the SQLite database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM data WHERE title = ?', (word,))
    result = cursor.fetchone()

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
        print("Not Found")
