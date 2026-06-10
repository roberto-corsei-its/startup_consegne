import numpy as np
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.scripts import get_connection
from src.utils import view_rider, inser_review, elimin_recensione, view_reviews, media_recensioni, update_comment


#POST
def inserimento_recensione(rider_id:int, customer_name:str, rating:int, comment:str):
    try:
        lista_rider = view_rider()
        if rider_id not in [rider[1] for rider in lista_rider]:
            inser_review(rider_id,customer_name,rating,comment)
            return jsonify({"Message:":"Success"}), 200
         
        else:
            return jsonify({"Error:":"Il rider selezionato non esiste, inserisci un id valido."})

    except ValueError:
        return jsonify({"Error:":"I dati inseriti non sono validi, assicurati di inserire un numero intero per rider_id e rating."}), 400
    except Exception as e:
        return jsonify({"Error:":str(e)}), 500
          

#DELETE
def eliminazione_recensione(rider_id:int):
    
    try:
       riders = view_rider()
       reviews = view_reviews()
       if rider_id not in [rider[0] for rider in riders] and rider_id not in [review[1] for review in reviews]:
            return jsonify({"Error:":"La recensione selezionata non esiste, inserisci un id valido."}), 400
       else:
            elimin_recensione(id)
            return jsonify({"Message:":"Recensione eliminata con successo."}), 200
            
    except ValueError:
        return jsonify({"Error:":"I dati inseriti non sono validi, assicurati di inserire un numero intero per id."}), 400
    except Exception as e:
        return jsonify({"Error:":str(e)}), 


def media_recens(rider_id:int):

    try:
        riders = view_rider()
        if rider_id not in [rider[0] for rider in riders]:
            return jsonify({'Error:':'Questo id rider non è presente'})
        else:
            return media_recensioni()
    except ValueError:
        return jsonify({"Error:":"I dati inseriti non sono validi, assicurati di inserire un numero intero per id."})
    except Exception as e:
        return jsonify({"Error:":str(e)}), 500

           
#AGGIORNAMENTO
def aggiornamento_recensione(id:int, comment:str):

    try:
        reviews = view_reviews()
        if id not in [review[0] for review in reviews]:
            
            return jsonify({'Error:':'Questo id non è presente tra le recensioni.'})
        else:  
            return update_comment(id, comment)
    except ValueError:
        return jsonify({"Error:":"I dati inseriti non sono validi, assicurati di inserire un numero intero per id."})
    except Exception as e:
        return jsonify({"Error:":str(e)}), 500
    

    
def visualizzazione_recensioni()):
    try:
        return view_reviews()
    except Exception as e:
        return jsonify({"Error:":str(e)}), 500


def aggiornamento_commenti(id:int, comment:str):
    try:
        reviews = view_reviews()
        if id not in [review[0] for review in reviews]:
            
            return jsonify({'Error:':'Questo id non è presente tra le recensioni.'})
        else:  
            return update_comment(id, comment)
    except ValueError:
        return jsonify({"Error:":"I dati inseriti non sono validi, assicurati di inserire un numero intero per id."})
    except Exception as e:
        return jsonify({"Error:":str(e)}), 500