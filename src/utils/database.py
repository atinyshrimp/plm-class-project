import sqlite3

def create_connection():
    """Create a database connection to the SQLite database."""
    connection = None
    try:
        connection = sqlite3.connect("plm_database.db")  # Use your database file name
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query, params=()):
    """Execute a single query."""
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

def fetch_all(connection, query, params=()):
    """Fetch all results from a query."""
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        return result