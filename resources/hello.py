from flask_restful import Resource
from flask import jsonify, request, make_response


class Hello(Resource):
    def get(self):
        """
            corresponds to the GET request.
            this function is called whenever there
            is a GET request for this resource
        """
        return jsonify({'message': 'hello world'})

    def post(self):
        """ Corresponds to POST request """
        data = request.get_json() # status code
        # print(data)
        return make_response(jsonify(data), 200)
