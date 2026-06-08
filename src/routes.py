from flask import Blueprint, request, jsonify


# Inizializzato il blueporint di consegne
consegne_bp = Blueprint('consegne', __name__, url_prefix='/consegne')

