from flask import Response
from flask_restful import Resource, reqparse
from flask_restplus import Resource
from src.app.middleware.auth import authenticate
from src.app.services.mongo import mongo_connection
from src.app.utils.verification import verification_sales_channel
from src.restplus import api, ns_wallet_listing


@ns_wallet_listing.route("/create")
class PostWalletListing(Resource):
    @authenticate
    @api.doc(description="Create a new wallet listing")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "wallet_listing_id", type=int, required=True, location="json"
        )
        parser.add_argument("name", type=str, required=True, location="json")
        parser.add_argument("type", type=str, required=True, location="json")
        parser.add_argument("commission", type=float, required=True, location="json")
        parser.add_argument(
            "sales_channel_id", type=int, required=True, location="json"
        )
        body = parser.parse_args()

        payload = {
            "wallet_listing_id": body["wallet_listing_id"],
            "name": body["name"],
            "type": body["type"],
            "commission": body["commission"],
            "sales_channel_id": body["sales_channel_id"],
        }

        try:
            if (
                verification_sales_channel(
                    type=body["type"], sales_channel_id=body["sales_channel_id"]
                )
                == True
            ):
                mongo_connection().wallet.insert_one(payload)
                return Response("success", status=200, mimetype="application/json")
            else:
                return Response("error", status=500, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_wallet_listing.route("/<wallet_listing_id>")
class GetWalletListing(Resource):
    @authenticate
    @api.doc(description="Get a wallet listing by id")
    def get(self, wallet_listing_id):
        try:
            payload = mongo_connection().wallet.find_one(
                {"wallet_listing_id": wallet_listing_id}
            )
            return Response(payload, status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_wallet_listing.route("/update/<wallet_listing_id>")
class PutWalletListing(Resource):
    @authenticate
    @api.doc(description="Update a wallet listing by id")
    def put(self, wallet_listing_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, location="json")
        parser.add_argument("type", type=str, required=True, location="json")
        parser.add_argument("commission", type=float, required=True, location="json")
        parser.add_argument(
            "sales_channel_id", type=str, required=True, location="json"
        )
        body = parser.parse_args()

        payload = {
            "name": body["name"],
            "type": body["type"],
            "commission": body["commission"],
            "sales_channel_id": body["sales_channel_id"],
        }

        try:
            if (
                verification_sales_channel(
                    type=body["type"], sales_channel_id=body["sales_channel_id"]
                )
                == True
            ):
                mongo_connection().wallet.update_one(
                    {"wallet_listing_id": wallet_listing_id}, {"$set": payload}
                )
                return Response("success", status=200, mimetype="application/json")
            else:
                return Response("error", status=500, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_wallet_listing.route("/delete/<wallet_listing_id>")
class DeleteWalletListing(Resource):
    @authenticate
    @api.doc(description="Delete a wallet listing by id")
    def delete(self, wallet_listing_id):
        try:
            mongo_connection().wallet.delete_one(
                {"wallet_listing_id": wallet_listing_id}
            )
            return Response("success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")
