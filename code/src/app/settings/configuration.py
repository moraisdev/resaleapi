# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


def get_env_variable(name):
    """Pick up the contents of environment variables."""
    try:
        return os.environ[name]
    except KeyError:
        raise KeyError(f"Expected environment variable '{name}' not set.")


class Configuration(object):
    """Interacting with environment variables."""

    FLASK_ENV = "Develop"
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(16)
    ASSETS_DEBUG = True
    RESTPLUS_VALIDATE = True

    ENV = get_env_variable("ENV")
    PORT = get_env_variable("PORT")
    TOKEN = get_env_variable("TOKEN")
    LOGGER = get_env_variable("LOGGER")
    LOGLEVEL = get_env_variable("LOGLEVEL")
    JWT_SECRET_KEY = get_env_variable("JWT_SECRET_KEY")

    MONGO_HOST = get_env_variable("MONGO_HOST")
    MONGO_PORT = get_env_variable("MONGO_PORT")
    MONGO_USER = get_env_variable("MONGO_USER")
    MONGO_PASS = get_env_variable("MONGO_PASS")

    MONGO_CONFIGS = {
        "host": MONGO_HOST,
        "port": MONGO_PORT,
        "username": MONGO_USER,
        "password": MONGO_PASS,
        "env": ENV,
    }
