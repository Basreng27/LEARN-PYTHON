# test_connection_pyodbc.py
import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_connection():
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    
    try:
        conn = pyodbc.connect(conn_str)
        print("Connection to SQL Server successful")
        return conn
    except pyodbc.Error as e:
        print(f"The error '{e}' occurred while connecting to the server '{server}' and database '{database}'")
        return None

# Test the connection
conn = create_connection()
if conn:
    conn.close()
