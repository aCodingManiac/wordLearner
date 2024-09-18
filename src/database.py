# src/database.py
import sqlite3

def getConnection():
    return sqlite3.connect('tracker.db')

def executeQuery(query, params=()):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    connection.close()
