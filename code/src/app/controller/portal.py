from flask import Response
from flask_restplus import Resource
from src.restplus import api, ns_portal_listing
from src.app.services.mongo import mongo_connection

@ns_portal_listing.route("")
class GetProperty(Resource):
    #@authenticate
    @api.doc(description="Get list portal")
    def get(self, property_id):
        try:
            return Response( str(result), status=200, mimetype="application/json")
        except Exception as e:
            return Response( str(e), status=500, mimetype="application/json")