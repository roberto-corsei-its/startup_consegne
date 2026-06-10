from flask import Blueprint, request, jsonify
from handlers.handler_recensioni import inserimento_recensione, eliminazione_recensione, media_recens, view_reviews
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
def aggiungi_recensione():
    try:
        # Ora prendi i dati dal body della richiesta di Postman
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Nessun dato JSON ricevuto nel body"}), 400
        rider_id = data.get('rider_id')
        customer_name = data.get('customer_name')
        rating = data.get('rating')
        comment = data.get('comment')
        inserimento_recensione(rider_id, customer_name, rating, comment)
        return jsonify({'message':'success'}), 200
        
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    




@consegne_bp.route('/delete/<id>', methods=['DELETE'])
def cancellazione_recensione(id):

    eliminazione_recensione(id)
    return jsonify({'message':'success'}), 200
    

@consegne_bp.route('/media/<rider_id>', methods=['GET'])
def media_reviews(rider_id):
    return jsonify(media_recens(rider_id))


@consegne_bp.route('/reviews', methods=['GET'])
def visualizzazione_recensioni():

    return jsonify(view_reviews())
    