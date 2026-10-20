from flask import Blueprint, jsonify
from src.models import get_welcome_message

api_bp = Blueprint('api', __name__)

@api_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify(get_welcome_message()), 200