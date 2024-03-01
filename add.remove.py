def remove_values_from_questions(questions, values_to_remove):
    """Remove specific values from the questions dictionary."""
    for question, answer in list(questions.items()):
        if answer in values_to_remove:
            questions.pop(question)

# Original dictionary variable
questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the powerhouse of the cell?": "Mitochondria",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}

# Values to remove
values_to_remove = ["Paris", "Mitochondria"]

# Remove values from the questions dictionary
remove_values_from_questions(questions, values_to_remove)

# Remove values from the dictionary
for question, answer in questions.items():
    if answer in values_to_remove:
        questions.pop(question)

print("Updated questions dictionary after removal:")
print(questions)

# Adding Variables
import sqlite3

def add_values_from_database(FridayProj5, questions):
    """Add values into the questions dictionary from the specified SQLite database."""
    # Connect to the SQLite database
    conn = sqlite3.connect(FridayProj5)
    cursor = conn.cursor()

    # Retrieve data from the database
    cursor.execute("SELECT question, answer FROM QuestAns")
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    # Add data into the questions dictionary
    for question, answer in data:
        questions[question] = answer

# Original dictionary variable
questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the powerhouse of the cell?": "Mitochondria",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}

# Example usage
db_file = "FridayProj5.db"  # Replace with the path to your SQLite database file
add_values_from_database(db_file, questions)

print("Updated questions dictionary with values from the database:")
print(questions)
