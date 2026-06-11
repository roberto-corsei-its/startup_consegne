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


#def create_table_db():
#    with get_connection() as conn:
#     with conn.cursor() as cur:
#        # Creazione tabella riders
#        cur.execute("""
#            CREATE TABLE riders(
#            id serial PRIMARY KEY,
#            name varchar(50) not null,
#            vehicle varchar(50) not null,
#            total_deliveries integer not null)
#        """)
#    
#        # Creazione tabella reviews
#        cur.execute("""
#            CREATE TABLE reviews(
#            id SERIAL,
#            rider_id integer not null ,
#            customer_name varchar(50) not null,
#            rating integer not null,
#            comment varchar(400) not null,
#            FOREIGN KEY (rider_id) references riders(id) ON DELETE CASCADE ON UPDATE CASCADE,
#            PRIMARY KEY(id))
#
#        """)
#    
#        conn.commit()
#
    #def populate_tables_db():
    #    with get_connection() as conn:
    #     with conn.cursor() as cur:
    #        # Popolamento tabella riders
    #        cur.execute("""
    #            INSERT INTO riders (name, vehicle) VALUES
    #            ('Mario Rossi', 'Bicicletta'),
    #            ('Luigi Bianchi', 'Motocicletta'),
    #            ('Giulia Verdi', 'Auto')
    #        ON CONFLICT DO NOTHING;
    #        """)
    #    
    #        conn.commit()