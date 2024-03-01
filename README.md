# FridayProject5

Step 1 - origQuizBowl
ChatGPT the Original Quiz Bowl becuase my original computer broke. 
Defines a dictionary questions with trivia questions as keys and their corresponding answers as values.
Defines a function run_quiz that runs the quiz using the provided questions.
Welcomes the user to the quiz.
Shuffles the questions to add randomness.
Iterates through each question, displaying it to the user and prompting for their answer.
Checks if the user's answer matches the correct answer and provides feedback.
Displays the quiz results, showing the number of correct answers out of the total questions.

Step 2 - insructions
Find Table name.
Connects to the SQLite database using sqlite3.connect.
Retrieves the names of all tables in the database using a SELECT name FROM sqlite_master WHERE type='table' SQL query.
Prints out the names of the tables.
Closes the connection to the database using conn.close(). 

Step 3.1 - add/remove
This code defines a function remove_values_from_questions that removes specific values from the questions dictionary. All other variables have been removed, and the function is directly called with the questions dictionary and the list of values to remove.

Step 3.2 - add/remove
We define a function add_values_from_database that retrieves data from the specified SQLite database and adds it into the questions dictionary.
The database file is connected to using sqlite3.connect.
Data is retrieved from the database using a SQL query.
The connection to the database is closed.
The retrieved data is added into the questions dictionary.
The function is called with the questions dictionary and the path to the SQLite database file.
Finally, the updated questions dictionary with values from the database is printed.