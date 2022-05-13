from flask import Response, current_app
from flask_restful import Resource, reqparse
from flask_restplus import Resource
from src.app.middleware.auth import authenticate
from src.restplus import api, ns_sales_channel


@ns_sales_channel.route("/create")
class PostSalesChannel(Resource):
    @authenticate
    @api.doc(description="Create a new sales channel")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "sales_channel_id", type=str, required=True, location="json"
        )
        parser.add_argument("name", type=list, required=True, location="json")
        parser.add_argument(
            "type_sales_channel", type=list, required=True, location="json"
        )
        body = parser.parse_args()

        payload = {
            "sales_channel_id": body["property_id"],
            "name": body["name"],
            "type_sales_channel": body["type_sales_channel"],
        }

        try:
            connection_mongo = current_app.config["MONGO"]["resale"]["sales_channel"]
            connection_mongo.insert(payload)
            return Response("success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_sales_channel.route("/<sales_channel_id>")
class GetSalesChannel(Resource):
    @authenticate
    @api.doc(description="Get a sales channel by id")
    def get(self, sales_channel_id):
        try:
            connection_mongo = current_app.config["MONGO"]["resale"]["sales_channel"]
            payload = connection_mongo.find_one({"sales_channel_id": sales_channel_id})
            return Response(payload, status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_sales_channel.route("/update/<sales_channel_id>")
class PutSalesChannel(Resource):
    @authenticate
    @api.doc(description="Update a sales channel by id")
    def put(self, sales_channel_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=list, required=True, location="json")
        parser.add_argument(
            "type_sales_channel", type=list, required=True, location="json"
        )
        body = parser.parse_args()

        payload = {
            "name": body["name"],
            "type_sales_channel": body["type_sales_channel"],
        }

        try:
            connection_mongo = current_app.config["MONGO"]["resale"]["sales_channel"]
            connection_mongo.update({"sales_channel_id": sales_channel_id}, payload)
            return Response("success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_sales_channel.route("/delete/<sales_channel_id>")
class DeleteSalesChannel(Resource):
    @authenticate
    @api.doc(description="Delete a sales channel by id")
    def delete(self, sales_channel_id):
        try:
            connection_mongo = current_app.config["MONGO"]["resale"]["sales_channel"]
            connection_mongo.remove({"sales_channel_id": sales_channel_id})
            return Response("success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")
