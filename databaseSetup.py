# database_setup.py
import sqlite3

def createTable():
    connection = sqlite3.connect('tracker.db')
    cursor = connection.cursor()

    # Create a table for vocabulary
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vocabulary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            meaning TEXT
        )
    ''')

    # Create a table for quizzes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')

    # Create a table for progress tracking
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            words_learned INTEGER NOT NULL,
            words_recalled INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    createTable()
