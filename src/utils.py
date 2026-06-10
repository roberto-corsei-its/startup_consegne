import numpy as np
import pandas as pd
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.scripts import get_connection
import pandas as pd




def inser_review(rider_id, customer_name, rating, comment):
    
    with get_connection() as conn:
     with conn.cursor() as cur:

      query = "INSERT INTO reviews (rider_id, customer_name, rating, comment) VALUES (%s, %s, %s, %s)"

      cur.execute(query, (rider_id, customer_name, rating, comment))

      conn.commit()



def view_rider():
    # Rinominato get_connection per usufruire della funzione .cursor
    with get_connection() as conn:
     with conn.cursor() as cur:

      query = "SELECT * FROM riders"

      df = pd.read_sql_query(query, conn)

    return df.to_dict(orient="records")   

def view_reviews():
    # Rinominato get_connection per usufruire della funzione .cursor
    with get_connection() as conn:
     with conn.cursor() as cur:

      query = "SELECT * FROM reviews"

      df = pd.read_sql_query(query, conn)

    return df.to_dict(orient="records")   


def elimin_recensione(id):
    
    with get_connection() as conn:
     with conn.cursor() as cur:

      query = "DELETE * FROM reviews WHERE id = %s"

      df = pd.read_sql_query(query, conn, params = [id])

def media_recensioni(rider_id:int):
    with get_connection() as conn:
     with conn.cursor() as cur:

      query = "SELECT AVG(rating) FROM reviews GROUP BY rider_id HAVING rider_id = %s"

      df = pd.read_sql_query(query, conn, params = [rider_id])

    return df.to_dict(orient="records")


def update_comment(id, comment):
    with get_connection() as conn:
     with conn.cursor() as cur:

      query = "UPDATE reviews SET comment = %s WHERE id = %s"

      cur.execute(query, (comment, id))

      conn.commit()