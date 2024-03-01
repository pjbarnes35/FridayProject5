# FridayProject5

Step 1 - origQuizBowl
ChatGPT the Original Quiz Bowl becuase my original computer broke. 

Step 2 - insructions
Find Table name. 

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