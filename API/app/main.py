# app/main.py
import sys
import os

# Add the project directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
from config.connection import create_connection

# Logging to console
logging.basicConfig(
    stream=sys.stdout,
    encoding='utf-8',
    format='%(levelname)s:%(message)s',
    level=logging.DEBUG
)

# Create Database Connection
conn = create_connection()
if conn:
    logging.info('Connected successfully')
    # Use the connection (execute queries, etc.)
    # Example: cursor = conn.cursor()
    # cursor.execute("SELECT @@version")
    # row = cursor.fetchone()
    # print(row)
    conn.close()
