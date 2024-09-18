# src/quizzes.py
from src.database import executeQuery, getConnection
import random

def addQuizQuestion(question, answer):
    query = "INSERT INTO quizzes (question, answer) VALUES (?, ?)"
    executeQuery(query, (question, answer))

def generateQuizQuestions():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vocabulary")
    words = cursor.fetchall()
    
    questions = []
    for word in words:
        question = f"What is the meaning of the word '{word[1]}'?"
        answer = word[2]
        questions.append((question, answer))
    
    return questions

def getAllQuizQuestions():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM quizzes")
    return cursor.fetchall()
