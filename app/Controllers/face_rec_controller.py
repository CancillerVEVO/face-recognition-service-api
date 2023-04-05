from flask import request
from marshmallow import Schema, fields
from flask_restful import Resource


class KnownSchema(Schema):
    image_url = fields.Str()
    label = fields.Str()


class RequestSchema(Schema):
    known = fields.Nested('KnownSchema', many=True, required=True)
    unknown = fields.Str(required=True)


request_schema = RequestSchema()


# ENDPOINT: "/face_rec
class FaceRecognition(Resource):
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400
        try:
            data = request_schema.load(json_data)
            return data
        except Exception as e:
            return {'message': str(e)}, 400
