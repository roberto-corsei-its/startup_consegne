from flask import Blueprint, request, jsonify
from handlers.handler_recensioni import inserimento_recensione
from handlers.handler_consegne import visualizzazione_rider, visualizzazione_rider_veicoli


# Inizializzato il blueporint di consegne
consegne_bp = Blueprint('consegne', __name__, url_prefix='/consegne')


@consegne_bp.route('/riders', methods=['GET'])
def visualizzazione_riders(vehicle):
    if vehicle:
        return jsonify(visualizzazione_rider_veicoli(vehicle))
    else:
        return jsonify(visualizzazione_rider())
    




@consegne_bp.route('/recensione', methods=['POST'])
def aggiungi_recensione(id, rider_id, customer_name, rating, comment):


    inserimento_recensione(id, rider_id, customer_name, rating, comment)
    return jsonify({'message':'success'}), 200