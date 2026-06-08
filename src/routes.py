from flask import Blueprint, request, jsonify


# Inizializzato il blueporint di consegne
consegne_bp = Blueprint('consegne', __name__, url_prefix='/consegne')


@consegne_bp.route('/recensione', methods=['POST'])
def aggiungi_recensione():
    