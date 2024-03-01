import random

# Define a dictionary with trivia questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the powerhouse of the cell?": "Mitochondria",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}

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

# Run the quiz
run_quiz(questions)
