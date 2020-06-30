from flask import Flask, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__, static_folder='dist/static')

# enable CORS
CORS(app)


@app.route('/api/pizzas')
def pizzas():
    return jsonify({
        'pizzas': [
            {
                'name': 'Pepperoni',
                'img_url': 'pepperoni',
                'price': '399',
                'description': 'American classic with spicy pepperoni, Mozzarella and signature tomato sauce',
            },
            {
                'name': 'Margherita',
                'img_url': 'margherita',
                'price': '299',
                'description': 'Traditional recipe with signature tomato sauce, Mozzarella, oregano and juicy tomatoes',
            },
            {
                'name': 'Four cheeses',
                'img_url': '4cheeses',
                'price': '299',
                'description': 'Traditional blend of cheeses: Mozzarella, soft fresh cheese, blue cheese, Reggianito with signature tomato sauce and spicy oregano',
            },
        ]
    })


@app.route('/')
def index():
    vuejs_html = '/app/dist/index.html'
    return send_file(vuejs_html)
