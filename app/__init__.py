# -*- coding: utf-8 -*-

import os
from datetime import timedelta
from flask import Flask
from flask_jwt import JWT
from app.security import autenticate, identify
from config import TIME_TOKEN_EXPIRATION, SQLALCHEMY_DATABASE_URI


def create_app(config_filename):
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static').replace('/app/', '/')
    app = Flask(__name__, static_folder=static_dir, static_url_path='/static')

    app.config.from_object(config_filename)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = app.config['SECRET_KEY']
    app.config['APPLICATION_PATH'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=TIME_TOKEN_EXPIRATION)
    app.config['PROPAGATE_EXCEPTIONS'] = True

    jwt = JWT(app, autenticate, identify)

    from app.models import db
    db.init_app(app)

    @app.after_request
    def apply_caching(response):
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, private"  # HTTP 1.1.
        response.headers["Pragma"] = "no-cache"  # HTTP 1.0.
        response.headers["Expires"] = "0"  # Proxies.
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "GET,PUT,POST,DELETE,PATCH,OPTIONS"
        return response

    from app.blueprints.main import main_blueprint
    from app.blueprints.revendedor import revendedor_blueprint
    from app.blueprints.venda import venda_blueprint


    app.register_blueprint(blueprint=main_blueprint, url_prefix="/")
    app.register_blueprint(blueprint=revendedor_blueprint, url_prefix="/revendedor")
    app.register_blueprint(blueprint=venda_blueprint, url_prefix="/venda")


    return app
