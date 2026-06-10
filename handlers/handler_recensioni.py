import numpy as np
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.scripts import get_connection
from src.utils import view_rider, inser_review, elimin_recensione, view_reviews, media_recensioni


#POST
def inserimento_recensione(rider_id:int, customer_name:str, rating:int, comment:str):
    try:
       lista_rider = view_rider()
       if rider_id not in [rider[1] for rider in lista_rider]:
          return jsonify({"Error:":"Il rider selezionato non esiste, inserisci un id valido."})
       else:
        inser_review(rider_id,customer_name,rating,comment)
        return jsonify({"Message:":"Success"}), 200
    except ValueError:
        return jsonify({"Error:":"I dati inseriti non sono validi, assicurati di inserire un numero intero per rider_id e rating."}), 400
    except Exception as e:
        return jsonify({"Error:":str(e)}), 500
          

#DELETE
def eliminazione_recensione(id:int):
    
    try:
       riders = view_rider()
       reviews = view_reviews()
       if rider_id not in [rider[0] for rider in riders] and rider_id not in [review[1] for review in reviews]:
          elimin_recensione(id)
          return jsonify({"Message:":"Recensione eliminata con successo."}), 200
       else:
            return jsonify({"Error:":"La recensione selezionata non esiste, inserisci un id valido."}), 400
    except ValueError:
        return jsonify({"Error:":"I dati inseriti non sono validi, assicurati di inserire un numero intero per id."}), 400
    except Exception as e:
        return jsonify({"Error:":str(e)}), 


def media_recens(rider_id:int):
    

    return media_recensioni()

           
