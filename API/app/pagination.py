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

def pagging(limit:int, offset:int = 0):
    conn = create_connection()

    if conn:
        try:
            cursor = conn.cursor()
            query = f"""SELECT * FROM test.test ORDER BY id OFFSET ? ROWS FETCH NEXT ? ROWS ONLY"""
            data = (offset, limit)

            cursor.execute(query, data)
            row = cursor.fetchall()
            
            return  logging.info(f"Record found: {row}")
        except pyodbc.Error as e:
            logging.error(f"Error getting data: {e}")
        finally:
            conn.close()
            logging.info("Connection closed")

pagging(10)
print("============================")
pagging(10, 10)
print("============================")
pagging(10, 20)