import pyodbc, logging, sys, sys, os, csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.connection import create_connection

# Set up logging
logging.basicConfig(
    stream=sys.stdout,
    encoding='utf-8',
    format='%(levelname)s:%(message)s',
    level=logging.DEBUG
)

def read_csv(filename:str) -> tuple:
    with open(filename, 'r') as f :
        reader = csv.reader(f)
        next(reader) # skip the header
        return [tuple(row) for row in reader]
    
def bulk_insert_from_csv(filename: str) -> None:
    data = read_csv(filename)
    if not data:
        logging.error("No data found in CSV file")
        return

    conn = create_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.fast_executemany = True
        insert_query = "INSERT INTO test.test (name) VALUES (?)"
        cursor.executemany(insert_query, data)
        conn.commit()
        logging.info(f"Bulk insert successful: {len(data)} records added")
    except pyodbc.Error as e:
        conn.rollback()
        logging.error(f"Error in bulk insert: {e}")
    finally:
        conn.close()
        logging.info("Connection closed")

bulk_insert_from_csv('file_csv/file_bulk.csv')