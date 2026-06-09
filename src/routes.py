from flask import Blueprint, request, jsonify
from handlers.handler_recensioni import inserimento_recensione, eliminazione_recensione
from handlers.handler_consegne import visualizzazione_rider, visualizzazione_rider_veicoli


# Inizializzato il blueporint di consegne
consegne_bp = Blueprint('consegne', __name__, url_prefix='/consegne')


@consegne_bp.route('/riders', methods=['GET'])
@consegne_bp.route('/riders/<vehicle>', methods=['GET'])
def visualizzazione_riders(vehicle=None):
    if vehicle:
        return jsonify(visualizzazione_rider_veicoli(vehicle))
    else:
        return jsonify(visualizzazione_rider())
    



@consegne_bp.route('/recensione', methods=['POST'])
def aggiungi_recensione(rider_id, customer_name, rating, comment):


    inserimento_recensione(rider_id, customer_name, rating, comment)
    return jsonify({'message':'success'}), 200




@consegne_bp.route('/delete/<id>', methods=['DELETE'])
def cancellazione_recensione(id):

    eliminazione_recensione(id)
    return jsonify({'message':'success'}), 200
    
