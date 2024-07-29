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

def update_data(name:str, id:int):
    conn = create_connection()

    if conn:
        try:
            cursor = conn.cursor()
            insert_query = """ UPDATE test.test SET name = ? WHERE id = ? """

            data = (name, id)

            cursor.execute(insert_query, data)
            conn.commit()
            logging.info("Success Update Data")
        except pyodbc.Error as e:
            conn.rollback()
            logging.error(f"Error Update data: {e}")
        finally:
            conn.close()
            logging.info("Connection closed")

update_data("UDIN PETOT", 5)