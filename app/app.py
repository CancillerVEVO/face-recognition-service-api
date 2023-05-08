from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from marshmallow import Schema, ValidationError, fields
from controllers.face_rec_controller import FaceRecognition

app = Flask(__name__)
api = Api(app)

api.add_resource(FaceRecognition, '/face_recognition')


if __name__ == "__main__":
    app.run(port=3000, debug=True)
