from flask import Flask
from flask_cors import CORS
from src.app.controller import namespaces
from src.app.settings import Configuration
from src.restplus import configure as config_api

app = Flask(__name__)


def create_app(config=Configuration):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)
    CORS(app, resources={r"*": {"origins": "*"}})
    config_api(app)

    for namespace in namespaces:
        app.api.add_namespace(namespace)

    return app
