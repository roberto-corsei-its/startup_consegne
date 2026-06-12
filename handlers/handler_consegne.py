import numpy as np
import pandas as pd
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.scripts import get_connection
import pandas as pd
from src.utils import view_rider


# Funzione che ci permette di vedere la lista rider, si usa GET
def visualizzazione_rider():
    return view_rider()


# Funnzione che ci permette di filtrare i rider in base al tipo di veicolo, si usa GET
def visualizzazione_rider_veicoli(vehicle: str):
    # Rinominato get_connection per usufruire della funzione .cursor
    try:
      with get_connection() as conn:
       with conn.cursor() as cur:

        query = "SELECT * FROM riders WHERE LOWER(vehicle) = LOWER(%s)"
        # Abbiamo usato pandas per eseguire la query e restituire un dataframe, che poi convertiamo in dizionario
        df = pd.read_sql_query(query, conn, params=[vehicle])
      # Convertito in dizionario con df.to_dict() e orientato per avere una lista di dizionari, uno per ogni riga del dataframe
        return df.to_dict(orient="records")
    except ValueError:
       return jsonify({"Error:":"Inserisci una stringa per il tipo di veicolo"}), 400
    except Exception as e:
       return jsonify({"Error:":str(e)}), 500