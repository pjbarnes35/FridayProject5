import sqlite3
import random

def get_questions_from_database(db_file):
    """Retrieve questions from the specified SQLite database."""
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Retrieve data from the database
    cursor.execute("SELECT question, answer FROM QuestAns")
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    # Convert the fetched data into a dictionary
    questions = {question: answer for question, answer in data}
    return questions

def run_quiz(questions):
    """Run the quiz with the provided questions."""
    print("Welcome to the Quiz!\n")

    # Shuffle the questions for added randomness
    shuffled_questions = list(questions.keys())
    random.shuffle(shuffled_questions)

    # Initialize variables to keep track of score
    total_questions = len(questions)
    correct_answers = 0

    # Iterate through each question
    for question in shuffled_questions:
        # Display the question and prompt for user input
        user_answer = input(question + "\nYour answer: ")

        # Check if the user's answer matches the correct answer
        if user_answer.lower() == questions[question].lower():
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Sorry, the correct answer is: {questions[question]}\n")

    # Display quiz results
    print(f"\nQuiz Complete!\nYou got {correct_answers} out of {total_questions} questions correct.")

# Example usage
db_file = "FridayProj5.db"  # Replace with the path to your SQLite database file

# Get questions from the database
questions = get_questions_from_database(db_file)

# Run the quiz with questions from the database
run_quiz(questions)
