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

# Read CSV
def read_csv(filename:str) -> tuple:
    with open(filename, 'r') as f :
        reader = csv.reader(f)
        next(reader) # skip the header
        return [tuple(row) for row in reader]

# Import To Table Database
def import_from_csv(filename: str) -> None:
    names = read_csv(filename)

    for name in names:
        insert(name[0])

def insert(name:str):
    conn = create_connection()

    if conn:
        try:
            cursor = conn.cursor()
            insert_query = """ INSERT INTO test.test (name) VALUES (?) """

            data = (name)

            cursor.execute(insert_query, data)
            conn.commit()
            logging.info(f"Success Add Data: {name}")
        except pyodbc.Error as e:
            conn.rollback()
            logging.error(f"Error inserting data: {e}")
        finally:
            conn.close()
            logging.info("Connection closed")

import_from_csv('file_csv/file_name.csv')
# Cek File Ada Atau Tidak
# filename = 'file_name.csv'

# if os.path.exists(filename):
#     with open(filename, 'r') as f:
#         print(f.read())
# else:
#     print(f"File {filename} tidak ditemukan.")