import pyodbc, logging, sys, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.connection import create_connection

# Set up logging
logging.basicConfig(
    stream=sys.stdout,
    encoding='utf-8',
    format='%(levelname)s:%(message)s',
    level=logging.DEBUG
)

def find_by_id(id: int):
    conn = create_connection()

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id, name FROM test.test WHERE id = ?"
            data = (id,)

            cursor.execute(query, data)
            row = cursor.fetchone()
            
            return  logging.info(f"Record found: {row}")
        except pyodbc.Error as e:
            logging.error(f"Error getting data: {e}")
        finally:
            conn.close()
            logging.info("Connection closed")

def find_all():
    conn = create_connection()

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id, name FROM test.test"

            cursor.execute(query)
            row = cursor.fetchall()
            
            return  logging.info(f"Record all found: {row}")
        except pyodbc.Error as e:
            logging.error(f"Error getting data: {e}")
        finally:
            conn.close()
            logging.info("Connection closed")

find_by_id(5)
find_all()