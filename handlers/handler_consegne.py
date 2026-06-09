import numpy as np
import pandas as pd
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.scripts import get_connection
import pandas as pd




def visualizzazione_rider():
    # Rinominato get_connection per usufruire della funzione .cursor
    with get_connection() as conn:
     with conn.cursor() as cur:

      query = "SELECT * FROM riders"

      df = pd.read_sql_query(query, conn)

    return df.to_dict(orient="records")   


def visualizzazione_rider_veicoli(vehicle):
    # Rinominato get_connection per usufruire della funzione .cursor
    with get_connection() as conn:
     with conn.cursor() as cur:

      query = "SELECT * FROM riders WHERE vehicle = %s"

      df = pd.read_sql_query(query, conn, params=[vehicle])

    return df.to_dict(orient="records")   