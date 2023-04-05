from flask import request
from marshmallow import Schema, fields
from flask_restful import Resource
from utils.download_face_data import download_face_data
from utils.remove_face_data import remove_face_data
from services.face_rec import recognize_face_in_image
import os
from uuid import uuid4


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
            path = os.path.join(os.getcwd(), 'temp', str(uuid4()))
            os.makedirs(path)

            image_path_and_label_pair, path_to_unknown_image = download_face_data(
                data, path)
            label = recognize_face_in_image(
                image_path_and_label_pair, path_to_unknown_image)

            if label:
                remove_face_data(path)
                return {'label': label}, 200
            else:
                remove_face_data(path)
                return {'message': 'No match found'}, 404
        except Exception as e:
            return {'message': str(e)}, 400
