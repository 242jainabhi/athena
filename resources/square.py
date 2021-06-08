from flask_restful import Resource
from flask import jsonify


class Square(Resource):
    def get(self, num):
        return num ** 2
