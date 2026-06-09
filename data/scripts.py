import psycopg
from psycopg.rows import dict_row
import os


DB_NAME = os.getenv('DB_NAME')
PORT = os.getenv('PORT')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

# Dati da configurare. WIP
DB_CONFIG = {
    "dbname": 'startup_consegne',
    "user": 'postgres',
    "password": 'Lagaeng02!',
    "host": "127.0.0.1",
    "port": '8082'
}


def get_connection():
    # Stabilisce la connessione
    return psycopg.connect(**DB_CONFIG, connect_timeout = 5)
