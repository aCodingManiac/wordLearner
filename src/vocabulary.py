import sqlite3

# Function to initialize the vocabulary table
def initializeDatabase():
    conn = sqlite3.connect('vocabulary.db')
    c = conn.cursor()
    # Create the vocabulary table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS vocabulary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            meaning TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def addVocabularyWord(word, meaning):
    conn = sqlite3.connect('vocabulary.db')
    c = conn.cursor()
    c.execute("INSERT INTO vocabulary (word, meaning) VALUES (?, ?)", (word, meaning))
    conn.commit()
    conn.close()

def getAllVocabularyWords():
    conn = sqlite3.connect('vocabulary.db')
    c = conn.cursor()
    c.execute("SELECT * FROM vocabulary")
    vocabularies = c.fetchall()
    conn.close()
    return vocabularies

def removeVocabularyWord(word):
    conn = sqlite3.connect('vocabulary.db')
    c = conn.cursor()
    c.execute("DELETE FROM vocabulary WHERE word = ?", (word,))
    conn.commit()
    conn.close()
