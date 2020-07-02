from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
from .extensions import db
from .commands import create_tables
from .routes import main


def create_app(config_file='settings.py'):
    app = Flask(__name__, static_folder='dist/static')
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.cli.add_command(create_tables)

    # enable CORS
    CORS(app)
    app.register_blueprint(main)
    return app
