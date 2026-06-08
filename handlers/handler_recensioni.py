import numpy as np
import pandas as pd
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.scripts import get_connection



REVIEW = os.getenv('REVIEW')


df = pd.read_csv(REVIEW)



def inserimento_recensione(id, rider_id, customer_name, rating, comment):
    # Rinominato get_connection per usufruire della funzione .cursor
    with get_connection() as conn:
     with conn.cursor() as cur:
      cur.execute("INSERT INTO reviews (id, rider_id, customer_name, rating, comment) VALUES (%s,%s,%s,%s,%s)", 
                  (id, rider_id, customer_name, rating, comment))
    conn.commit()
    # Inserimento dei dati nel DB attraverso una query INSERT.         
