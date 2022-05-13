# -*- coding: utf-8 -*-

from flask_restplus import Api
from src.app.settings import Configuration


class Server(object):
    def __init__(self):
        self.api = Api(
            version="1.0.0",
            title="API",
            description="Swagger domumentation from resale application",
            contact="email Pedro Morais",
            contact_email="pedrolukasmorais@gmail.com",
            doc=self.environments[Configuration.ENV]["swagger-url"],
            security="Bearer Auth",
            authorizations=self.authorizations,
        )

    @property
    def environments(self):
        return {
            "development": {"debug": True, "swagger-url": "/doc"},
            "sandbox": {"debug": True, "swagger-url": "/doc"},
            "production": {"debug": False, "swagger-url": None},
        }

    @property
    def authorizations(self):
        return {
            "Bearer Auth": {"type": "apiKey", "in": "header", "name": "Authorization"},
        }


api = Server().api

ns_property = api.namespace("property")
ns_sales_channel = api.namespace("sales_channel")
ns_house_listing = api.namespace("house_listing")


def configure(app):
    api.init_app(app)
    app.api = api
