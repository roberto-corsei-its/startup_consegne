import numpy as np
import pandas as pd
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.scripts import get_connection
import pandas as pd
from src.utils import view_rider



def visualizzazione_rider():
    #try:
        return view_rider()
    #except Exception as e:
       # return jsonify({"Error:":str(e)}), 500


def visualizzazione_rider_veicoli(vehicle: str):
    # Rinominato get_connection per usufruire della funzione .cursor
    try:
      with get_connection() as conn:
       with conn.cursor() as cur:

        query = "SELECT * FROM riders WHERE LOWER(vehicle) = LOWER(%s)"

        df = pd.read_sql_query(query, conn, params=[vehicle])

      return df.to_dict(orient="records")
    except ValueError:
       return jsonify({"Error:":"Inserisci una stringa per il tipo di veicolo"}), 400
    except Exception as e:
       return jsonify({"Error:":str(e)}), 500