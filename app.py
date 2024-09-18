# app.py
import streamlit as st
from src.vocabulary import addVocabularyWord, getAllVocabularyWords, removeVocabularyWord
from src.quizzes import addQuizQuestion, generateQuizQuestions, getAllQuizQuestions
from src.progress import addProgressEntry, getWeeklyProgress, getStreak

def addVocabularyPage():
    st.header("Add Vocabulary")
    word = st.text_input("Enter a new vocabulary word")
    meaning = st.text_input("Enter the meaning")

    # Input validation for adding vocabulary
    if st.button("Add Vocabulary"):
        if not word.strip() or not meaning.strip():
            st.error("Error: Both word and meaning must be provided!")
        else:
            addVocabularyWord(word, meaning)
            st.success("Vocabulary word added successfully!")

    st.subheader("Vocabulary List")
    vocabularies = getAllVocabularyWords()
    if vocabularies:
        for vocab in vocabularies:
            st.write(f"Word: {vocab[1]}, Meaning: {vocab[2]}")
    else:
        st.warning("No vocabulary words added yet.")

    # Search functionality with error checking
    st.subheader("Search Vocabulary")
    searchTerm = st.text_input("Search for a word")
    if searchTerm:
        vocabularies = [vocab for vocab in getAllVocabularyWords() if searchTerm.lower() in vocab[1].lower()]
        if vocabularies:
            for vocab in vocabularies:
                st.write(f"Word: {vocab[1]}, Meaning: {vocab[2]}")
        else:
            st.error("No vocabulary found for this search term.")

    # New section for removing a vocabulary word
    st.subheader("Remove Vocabulary Word")
    words = [vocab[1] for vocab in vocabularies]
    selectedWord = st.selectbox("Select a word to remove", words)
    
    if st.button("Remove Word"):
        if selectedWord:
            removeVocabularyWord(selectedWord)
            st.success(f"'{selectedWord}' has been removed from the vocabulary list.")
        else:
            st.error("Error: Please select a word to remove.")

def generateQuizPage():
    st.header("Generate Quiz Questions")

    # Generating quiz questions
    if st.button("Generate Quizzes"):
        questions = generateQuizQuestions()
        if questions:
            for q in questions:
                addQuizQuestion(q[0], q[1])
            st.success("Quiz questions generated successfully!")
        else:
            st.error("No vocabulary available to generate quiz questions.")

    st.subheader("Quiz Questions List")
    quizzes = getAllQuizQuestions()
    if quizzes:
        for quiz in quizzes:
            st.write(f"Question: {quiz[1]}, Answer: {quiz[2]}")
    else:
        st.warning("No quiz questions available yet.")

def progressTrackingPage():
    st.header("Progress Tracking")

    # Adding progress entries with error handling
    st.subheader("Add Progress Entry")
    wordsLearned = st.number_input("Number of words learned today", min_value=0, step=1)
    wordsRecalled = st.number_input("Number of words recalled today", min_value=0, step=1)

    if st.button("Submit Progress"):
        if wordsLearned == 0 and wordsRecalled == 0:
            st.error("Error: You must enter at least one word learned or recalled.")
        else:
            addProgressEntry(wordsLearned, wordsRecalled)
            st.success("Progress entry added successfully!")

    # Display weekly progress
    st.subheader("Weekly Progress")
    weeklyProgress = getWeeklyProgress()
    if weeklyProgress:
        for entry in weeklyProgress:
            st.write(f"Date: {entry[1]}, Words Learned: {entry[2]}, Words Recalled: {entry[3]}")
    else:
        st.warning("No progress data available for the past week.")

    # Streak tracking
    st.subheader("Streak")
    streak = getStreak()
    st.write(f"Current Study Streak: {streak} days")

# Main function to manage tabs
def main():
    st.title("Language Learning Tracker")

    # Tabs for navigation
    tabNames = ["Add Vocabulary", "Generate Quiz", "Progress Tracking"]
    selectedTab = st.sidebar.selectbox("Select a page", tabNames)

    if selectedTab == "Add Vocabulary":
        addVocabularyPage()
    elif selectedTab == "Generate Quiz":
        generateQuizPage()
    elif selectedTab == "Progress Tracking":
        progressTrackingPage()

if __name__ == "__main__":
    main()
