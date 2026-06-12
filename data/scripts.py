import psycopg
from psycopg.rows import dict_row
import os

# Creazione dizionario con valori di connessione al database presi dal .env
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT")
}

# Funzione di connessione al database
def get_connection():
    return psycopg.connect(**DB_CONFIG, connect_timeout=5)

# Creazione delle tabelle
def create_table_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            # Creazione tabella riders
            cur.execute("""
                CREATE TABLE IF NOT EXISTS riders(
                id serial PRIMARY KEY,
                name varchar(50) not null UNIQUE,
                vehicle varchar(50) not null,
                total_deliveries integer not null);
            """)
            
            # Creazione tabella reviews
            cur.execute("""
                CREATE TABLE IF NOT EXISTS reviews(
                id SERIAL,
                rider_id integer not null,
                customer_name varchar(50) not null,
                rating integer not null,
                comment varchar(400) not null,
                FOREIGN KEY (rider_id) references riders(id) ON DELETE CASCADE ON UPDATE CASCADE,
                PRIMARY KEY(id));
            """)
    # Il commit avviene in automatico qui all'uscita del 'with'

def populate_tables_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            # Popolamento tabella riders
            cur.execute("""
                INSERT INTO riders(name, vehicle, total_deliveries) VALUES
                ('Mario Rossi', 'Bicicletta', 120),
                ('Luigi Bianchi', 'Motocicletta', 90),
                ('Giulia Verdi', 'Auto', 19912)
                ON CONFLICT (name) DO NOTHING; 
            """)
    # Il commit avviene in automatico qui all'uscita del 'with'