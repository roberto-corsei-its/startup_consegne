import psycopg
from psycopg.rows import dict_row
import os


DB_NAME = os.getenv('DB_NAME')
PORT = os.getenv('PORT')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

# Dati da configurare. WIP
DB_CONFIG = {
    "dbname": DB_NAME,
    "user": USER,
    "password": PASSWORD,
    "host": "localhost",
    "port": PORT
}


def get_connection():
    # Stabilisce la connessione
    return psycopg.connect(**DB_CONFIG, row_factory=dict_row)