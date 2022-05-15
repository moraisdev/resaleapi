from flask import Response
from flask_restful import reqparse
from flask_restplus import Resource
from src.restplus import api, ns_property
from src.app.services.mongo import mongo_connection
@ns_property.route("/create")
class PostProperty(Resource):
    @api.doc(description="Create a new property")
    #@authenticate
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("property_id", type=str, required=True, location="json")
        parser.add_argument("name", type=str, required=True, location="json")
        parser.add_argument("address", type=str, required=True, location="json")
        parser.add_argument("description", type=str, required=True, location="json")
        parser.add_argument("status", type=bool, required=True, location="json")
        parser.add_argument("characteristics", type=str, required=True, location="json")
        parser.add_argument("type", type=str, required=True, location="json")
        parser.add_argument("purpose", type=str, required=True, location="json")
        parser.add_argument("evaluated_value", type=float, required=True, location="json")
        parser.add_argument("property_value", type=float, required=True, location="json")
        body = parser.parse_args()
        
        payload = {
                "property_id": body["property_id"],
                "name": body["name"],
                "address": body["address"],
                "description":body["description"],
                "status": body["status"],
                "characteristics": body["characteristics"],
                "type": body["type"],
                "purpose": body["purpose"],
                "evaluated_value": body["evaluated_value"],
                "property_value": body["property_value"]
        }

        try:
            mongo_connection().property.insert_one(payload)
            return Response( "success", status=200, mimetype="application/json")
        except Exception as e:
            return Response(str(e), status=500, mimetype="application/json")

@ns_property.route("/<string:property_id>")
class GetProperty(Resource):
    #@authenticate
    @api.doc(description="Route to return property")
    def get(self, property_id):
        try:
            result = mongo_connection().property.find_one({"property_id": property_id})
            return Response( str(result), status=200, mimetype="application/json")
        except Exception as e:
            return Response( str(e), status=500, mimetype="application/json")

@ns_property.route("/update/<string:property_id>")
class PutProperty(Resource):
    #@authenticate
    @api.doc(description="Route to update property")
    def put(self, property_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, location="json")
        parser.add_argument("address", type=str, required=True, location="json")
        parser.add_argument("description", type=str, required=True, location="json")
        parser.add_argument("status", type=bool, required=True, location="json")
        parser.add_argument("characteristics", type=str, required=True, location="json")
        parser.add_argument("type", type=str, required=True, location="json")
        parser.add_argument("purpose", type=str, required=True, location="json")
        parser.add_argument("evaluated_value", type=float, required=True, location="json")
        parser.add_argument("property_value", type=float, required=True, location="json")
        body = parser.parse_args()
        
        payload = {
                "property_id": property_id,
                "name": body["name"],
                "address": body["address"],
                "description":body["description"],
                "status": body["status"],
                "characteristics": body["characteristics"],
                "type": body["type"],
                "purpose": body["purpose"],
                "evaluated_value": body["evaluated_value"],
                "property_value": body["property_value"]
        }

        try:
            mongo_connection().property.update_one({"property_id": property_id}, {"$set": payload})
            return Response( "success", status=200, mimetype="application/json")
        except Exception as e:
            return Response( str(e), status=500, mimetype="application/json")

@ns_property.route("/delete/<string:property_id>")
class DeleteProperty(Resource):
    #@authenticate
    @api.doc(description="Route to delete property")
    def get(self, property_id):
        try:
            mongo_connection().property.delete_one({"property_id": property_id})
            return Response( "success", status=200, mimetype="application/json")
        except Exception as e:
            return Response( str(e), status=500, mimetype="application/json")