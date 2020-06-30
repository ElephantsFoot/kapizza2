from flask import Flask, jsonify, send_file, request
from flask_cors import CORS

app = Flask(__name__, static_folder='dist/static')

# enable CORS
CORS(app)


@app.route('/api/pizzas', methods=['GET'])
def pizzas():
    return jsonify({
        'pizzas': [
            {
                'name': 'Pepperoni',
                'img_url': 'pepperoni',
                'price': 14.99,
                'description': 'American classic with spicy pepperoni, Mozzarella and signature tomato sauce',
            },
            {
                'name': 'Margherita',
                'img_url': 'margherita',
                'price': 13.99,
                'description': 'Traditional recipe with signature tomato sauce, Mozzarella, oregano and juicy tomatoes',
            },
            {
                'name': 'Four cheeses',
                'img_url': '4cheeses',
                'price': 11.99,
                'description': 'Traditional blend of cheeses: Mozzarella, soft fresh cheese, blue cheese, Reggianito with signature tomato sauce and spicy oregano',
            },
        ]
    })


@app.route('/')
def index():
    vuejs_html = '/app/dist/index.html'
    return send_file(vuejs_html)


@app.route('/api/place_order', methods=['POST'])
def place_order():
    from pprint import pprint
    pprint(request.json)
    return jsonify({})
