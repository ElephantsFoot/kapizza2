from flask import Blueprint, send_file, jsonify, request

from .extensions import db
from .models import Pizza

main = Blueprint('main', __name__)


@main.route('/')
def index():
    vuejs_html = '/app/dist/index.html'
    return send_file(vuejs_html)


@main.route('/api/pizzas', methods=['GET'])
def pizzas():
    pizzas = [pizza.__dict__ for pizza in Pizza.query.all()]
    for pizza in pizzas:
        pizza.pop('_sa_instance_state')
    return jsonify({
        'pizzas': pizzas
    })

@main.route('/api/place_order', methods=['POST'])
def place_order():
    from pprint import pprint
    pprint(request.json)
    return jsonify({})
