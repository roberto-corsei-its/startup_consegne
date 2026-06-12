from dotenv import load_dotenv
from src.app import create_app
from data.scripts import get_connection, create_table_db, populate_tables_db
import os

# Caricamento delle variabili d'ambiente
load_dotenv()

# Si prende la porta dal .env
PORT = int(os.getenv('PORT', '5000')) # È buona pratica convertirla in int

app = create_app()

# Inizializzazione dell'app
if __name__ == "__main__":
    # 1. Prima prepari il database
    print("Inizializzazione del database...")
    get_connection()
    create_table_db()
    populate_tables_db()
    
    # 2. Poi avvii il server web
    print(f"Avvio dell'applicazione sulla porta {PORT}...")
    app.run(host='0.0.0.0', port=PORT, debug=True)