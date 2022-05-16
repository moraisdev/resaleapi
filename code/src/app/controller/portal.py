import json

from flask import Response
from flask_restful import reqparse
from flask_restplus import Resource
from src.app.middleware.auth import authenticate
from src.app.services.mongo import mongo_connection
from src.app.utils.verification import list_portal, verification_wallet_listing
from src.restplus import api, ns_portal_listing


@ns_portal_listing.route("/associate")
class PostAssociate(Resource):
    @authenticate
    @api.doc(description="Associate property to wallet")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("property_id", type=int, required=True, location="json")
        parser.add_argument(
            "wallet_listing_id", type=list, required=True, location="json"
        )
        body = parser.parse_args()

        payload = {
            "property_id": body["property_id"],
            "wallet_listing_id": body["wallet_listing_id"],
        }
        try:
            if (
                verification_wallet_listing(wallet_listing_id=body["wallet_listing_id"])
                == True
            ):
                mongo_connection().associate.insert_one(payload)
                return Response("success", status=200, mimetype="application/json")
            else:
                return Response("error", status=500, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")


@ns_portal_listing.route("/list")
class GetPortalList(Resource):
    @authenticate
    @api.doc(description="Get all portal listings")
    def get(self):
        try:
            payload = list_portal()
            return Response(str(payload), status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")
