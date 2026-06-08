import numpy as np
import pandas as pd
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.db_connection import get_connection



REVIEW = os.getenv('REVIEW')


df = pd.read_csv(REVIEW)



def inserimento_recensione(id, rider_id, customer_name, rating, comment):
    # Rinominato get_connection per usufruire della funzione .cursor
    with get_connection() as conn:
     with conn.cursor() as cur:
<<<<<<< HEAD
      cur.execute("INSERT INTO reviews (id, rider_id, customer_name, rating, comment) VALUES (%s,%s,%s,%s,%s)", (id, rider_id, customer_name, rating, comment))
    # Inserimento dei dati nel DB attraverso una query INSERT.           
=======
      cur.execute("INSERT INTO reviews (id, rider_id, customer_name, rating, comment) VALUES (%s,%s,%s,%s,%s)", 
                  (id, rider_id, customer_name, rating, comment))
    conn.commit()
    # Inserimento dei dati nel DB attraverso una query INSERT.         
>>>>>>> ad5fac8fb4cd9f0bcb7eaad834b3c3ce8ae8f1cb
