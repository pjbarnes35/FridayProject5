import sqlite3

def display_tables(FridayProj5):
    """Display the names of all tables in the database."""
    # Connect to the SQLite database
    conn = sqlite3.connect(FridayProj5)
    cursor = conn.cursor()

    # Retrieve table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    # Print table names
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # Close the connection
    conn.close()

# Example usage
db_file = "FridayProj5.db"  # Replace with the path to your SQLite database file
display_tables(db_file)

# Tables = QuestAns