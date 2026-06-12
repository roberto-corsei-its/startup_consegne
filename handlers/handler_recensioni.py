import numpy as np
from flask import Blueprint, request, jsonify
import os
import psycopg
from data.scripts import get_connection
from src.utils import view_rider, inser_review, elimin_recensione, view_reviews, media_recensioni, update_comment



# Le funzioni in handlers prendono le richieste controllate da routes, ed effettuano controlli sui dati effettivi
# Per poi delegare le query in src.utils


# Funzione per inserire le recensioni, con appropriati controlli
def inserimento_recensione(rider_id:int, customer_name:str, rating:int, comment:str):
    try:
        lista_rider = view_rider()
        if rider_id not in [rider[1] for rider in lista_rider]:
            if [rating <= 5 and rating >= 1]:
                inser_review(rider_id,customer_name,rating,comment)
                return jsonify({"Message:":"Success"}), 200
            else:
                return jsonify({'Error':'Il valore di rating da inserire deve essere tra 1 e 5'})
            
         
        else:
            return jsonify({"Error:":"Il rider selezionato non esiste, inserisci un id valido."})

    except ValueError:
        return jsonify({"Error:":"I dati inseriti non sono validi, assicurati di inserire un numero intero per rider_id e rating."}), 400
    except Exception as e:
        return jsonify({"Error:":str(e)}), 500
          

# Funzione per eliminare una recensione 
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

# Funzione per la media delle recensioni di un rider, controlla l'esistenza del rider
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

    

# Funzione per visualizzare le recensioni, si usa GET
def visualizzazione_recensioni():
    try:
        return view_reviews()
    except Exception as e:
        return jsonify({"Error:":str(e)}), 500

# Funzione per aggiorare i commenti di una recensione, si usa PUT, controlla che ci sia una recensione con il rider_id indicato
# Per poi controllare che il nome fornito esista
def aggiornamento_commenti(id:int, comment:str, nome:str):
    try:
        reviews = view_reviews()
        if id not in [review[0] for review in reviews]:
            return jsonify({'Error:':'Questo id non è presente tra le recensioni.'})
        elif nome not in[review[2] for review in reviews]:
            return jsonify({'Error:':'Non è presente una recensione con questo nome'})
        else:  
            return update_comment(id, comment, nome)
    except ValueError:
        return jsonify({"Error:":"I dati inseriti non sono validi, assicurati di inserire un numero intero per id."})
    except Exception as e:
        return jsonify({"Error:":str(e)}), 500