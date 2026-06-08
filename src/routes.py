from flask import Blueprint, request, jsonify
from handlers.handler_recensioni import inserimento_recensione


# Inizializzato il blueporint di consegne
consegne_bp = Blueprint('consegne', __name__, url_prefix='/consegne')


@consegne_bp.route('/recensione', methods=['POST'])
def aggiungi_recensione(id, rider_id, customer_name, rating, comment):


    inserimento_recensione(id, rider_id, customer_name, rating, comment)
    return jsonify({'message':'success'}), 200