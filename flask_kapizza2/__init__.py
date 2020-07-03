from flask import Flask, jsonify, request
from flask_cors import CORS
from .extensions import db
from .commands import create_tables
from .models import Pizza


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.cli.add_command(create_tables)

    # enable CORS
    CORS(app)

    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    
    @app.route('/api/pizzas', methods=['GET'])
    def pizzas():
        pizzas = [pizza.__dict__ for pizza in Pizza.query.all()]
        for pizza in pizzas:
            pizza.pop('_sa_instance_state')
        return jsonify({
            'pizzas': pizzas
        })

    @app.route('/api/place_order', methods=['POST'])
    def place_order():
        from pprint import pprint
        pprint(request.json)
        return jsonify({})

    return app
