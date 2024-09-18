# src/progress.py
from src.database import executeQuery, getConnection
from datetime import datetime, timedelta

def addProgressEntry(words_learned, words_recalled):
    date = datetime.now().strftime("%Y-%m-%d")
    query = "INSERT INTO progress (date, words_learned, words_recalled) VALUES (?, ?, ?)"
    executeQuery(query, (date, words_learned, words_recalled))

def getWeeklyProgress():
    connection = getConnection()
    cursor = connection.cursor()
    week_start = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    cursor.execute("SELECT * FROM progress WHERE date >= ?", (week_start,))
    return cursor.fetchall()

def getStreak():
    connection = getConnection()
    cursor = connection.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    streak = 0
    while True:
        cursor.execute("SELECT * FROM progress WHERE date = ?", (today,))
        if cursor.fetchone():
            streak += 1
            today = (datetime.strptime(today, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            break
    return streak
