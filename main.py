from dotenv import load_dotenv
from src.app import create_app
from data.scripts import get_connection, create_table_db
import os

# Caricamento delle variabili d'ambiente
load_dotenv()



# Si prende la porta dal .env
PORT = os.getenv('PORT', '5000')


app = create_app()
# Inizializzazione dell'app
if __name__ == "__main__":

    app.run(host='0.0.0.0', port=PORT, debug=True) 
    # (host='0.0.0.0', port=PORT, debug=True) per il debug in caso di problemi

get_connection()
create_table_db()


