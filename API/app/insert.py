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

def insert_data():
    conn = create_connection()

    if conn:
        try:
            cursor = conn.cursor()
            insert_query = """ INSERT INTO test.test (name) VALUES (?) """

            data = ("testing_insert_2")

            cursor.execute(insert_query, data)
            conn.commit()
            logging.info("Success Add Data")
        except pyodbc.Error as e:
            logging.error(f"Error inserting data: {e}")
        finally:
            conn.close()
            logging.info("Connection closed")

# Run the insert_data function
if __name__ == "__main__":
    insert_data()