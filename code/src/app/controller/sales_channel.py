from flask import Response
from flask_restful import reqparse
from flask_restplus import Resource
from src.app.middleware.auth import authenticate
from src.restplus import api, ns_sales_channel
from src.app.services.mongo import mongo_connection

@ns_sales_channel.route("/create")
class PostSalesChannel(Resource):
    @authenticate
    @api.doc(description="Create a new sales channel")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("sales_channel_id", type=str, required=True, location="json")
        parser.add_argument("name", type=str, required=True, location="json")
        parser.add_argument("type_sales_channel", type=str, required=True, location="json")
        body = parser.parse_args()

        payload = {
            "sales_channel_id": body["property_id"],
            "name": body["name"],
            "type_sales_channel": body["type_sales_channel"],
        }

        try:
            mongo_connection().channel.insert_one(payload)
            return Response("success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_sales_channel.route("/<sales_channel_id>")
class GetSalesChannel(Resource):
    @authenticate
    @api.doc(description="Get a sales channel by id")
    def get(self, sales_channel_id):
        try:
            payload = mongo_connection().channel.find_one({"sales_channel_id": sales_channel_id})
            return Response(payload, status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_sales_channel.route("/update/<sales_channel_id>")
class PutSalesChannel(Resource):
    @authenticate
    @api.doc(description="Update a sales channel by id")
    def put(self, sales_channel_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, location="json")
        parser.add_argument(
            "type_sales_channel", type=str, required=True, location="json"
        )
        body = parser.parse_args()

        payload = {
            "name": body["name"],
            "type_sales_channel": body["type_sales_channel"],
        }

        try:
            mongo_connection().property.update_one({"sales_channel_id": sales_channel_id}, {"$set": payload})
            return Response("success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_sales_channel.route("/delete/<sales_channel_id>")
class DeleteSalesChannel(Resource):
    @authenticate
    @api.doc(description="Delete a sales channel by id")
    def delete(self, sales_channel_id):
        try:
            mongo_connection().property.delete_one({"sales_channel_id": sales_channel_id})
            return Response("success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")
