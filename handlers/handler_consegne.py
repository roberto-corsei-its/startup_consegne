import numpy as np
import pandas as pd
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.scripts import get_connection



REVIEW = os.getenv('REVIEW')


df = pd.read_csv(REVIEW)



def visualizzazione_rider():
    # Rinominato get_connection per usufruire della funzione .cursor
    with get_connection() as conn:
     with conn.cursor() as cur:
      return cur.execute("SELECT * FROM riders")
    conn.commit()
    # Inserimento dei dati nel DB attraverso una query INSERT.         


def visualizzazione_rider_veicoli(vehicle):
    # Rinominato get_connection per usufruire della funzione .cursor
    with get_connection() as conn:
     with conn.cursor() as cur:
      return cur.execute("SELECT * FROM riders WHERE vehicle =", (vehicle))
    conn.commit()
    # Inserimento dei dati nel DB attraverso una query INSERT.         