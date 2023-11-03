from database import data
import os
import sqlite3

DATABASE_PATH_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database.db'))


# //!Only the developers can enter the data if the DEVELOPMENT flag is set to True!!!
DEVELOPMENT = False 

if DEVELOPMENT:
    def insertData(title:str, pos:str, englishMeaning:str, kashmiriMeaning:str, englishExample:str = None, kashmiriExample:str = None):
        conn = sqlite3.connect(DATABASE_PATH_FILE)
        cursor = conn.cursor()
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
        cursor.execute('''INSERT INTO data (title, pos, englishMeaning, kashmiriMeaning, englishExample, kashmiriExample)
                        VALUES (?, ?, ?, ?, ?, ?)''', (title, pos, englishMeaning, kashmiriMeaning, englishExample, kashmiriExample))
        conn.commit()
        conn.close()