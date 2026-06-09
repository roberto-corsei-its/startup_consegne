import numpy as np
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.scripts import get_connection


#POST
def inserimento_recensione(rider_id, customer_name, rating, comment):
    
    with get_connection() as conn:
     with conn.cursor() as cur:

      query = "INSERT INTO reviews (rider_id, customer_name, rating, comment) VALUES (%s, %s, %s, %s)"

      df = pd.read_sql_query(query, conn, params = [rider_id, customer_name, rating, comment])

#DELETE
def eliminazione_recensione(id):
    
    with get_connection() as conn:
     with conn.cursor() as cur:

      query = "DELETE * FROM reviews WHERE id = %s"

      df = pd.read_sql_query(query, conn, params = [id])
           
