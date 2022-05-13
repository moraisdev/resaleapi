from flask import Response, current_app
from flask_restful import Resource, reqparse
from flask_restplus import Resource
from src.app.middleware.auth import authenticate
from src.restplus import api, ns_house_listing


@ns_house_listing.route("/create")
class PostHouseListing(Resource):
    @authenticate
    @api.doc(description="Create a new house listing")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "house_listing_id", type=str, required=True, location="json"
        )
        parser.add_argument("name", type=list, required=True, location="json")
        parser.add_argument("type", type=list, required=True, location="json")
        parser.add_argument("commission", type=list, required=True, location="json")
        parser.add_argument("sales_channel", type=list, required=True, location="json")
        body = parser.parse_args()

        payload = {
            "house_listing_id": body["house_listing_id"],
            "name": body["name"],
            "type": body["type"],
            "commission": body["commission"],
            "sales_channel": body["sales_channel"],
        }

        try:
            connection_mongo = current_app.config["MONGO"]["resale"]["house_listing"]
            connection_mongo.insert(payload)
            return Response("success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_house_listing.route("/<house_listing_id>")
class GetHouseListing(Resource):
    @authenticate
    @api.doc(description="Get a house listing by id")
    def get(self, house_listing_id):
        try:
            connection_mongo = current_app.config["MONGO"]["resale"]["house_listing"]
            payload = connection_mongo.find_one({"house_listing_id": house_listing_id})
            return Response(payload, status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_house_listing.route("/update/<house_listing_id>")
class PutHouseListing(Resource):
    @authenticate
    @api.doc(description="Update a house listing by id")
    def put(self, house_listing_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=list, required=True, location="json")
        parser.add_argument("type", type=list, required=True, location="json")
        parser.add_argument("commission", type=list, required=True, location="json")
        parser.add_argument("sales_channel", type=list, required=True, location="json")
        body = parser.parse_args()

        payload = {
            "name": body["name"],
            "type": body["type"],
            "commission": body["commission"],
            "sales_channel": body["sales_channel"],
        }

        try:
            connection_mongo = current_app.config["MONGO"]["resale"]["house_listing"]
            connection_mongo.update({"house_listing_id": house_listing_id}, payload)
            return Response("success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_house_listing.route("/delete/<house_listing_id>")
class DeleteHouseListing(Resource):
    @authenticate
    @api.doc(description="Delete a house listing by id")
    def delete(self, house_listing_id):
        try:
            connection_mongo = current_app.config["MONGO"]["resale"]["house_listing"]
            connection_mongo.remove({"house_listing_id": house_listing_id})
            return Response("success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")
