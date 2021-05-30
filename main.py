# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


@app.route('/greet/<name>')
def greeting(name):
    return 'Hi %s!!!' % name


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
        return jsonify({'data': data}), 201


# # another resource to calculate the square of a number
class Square(Resource):
    def get(self, num):
        return jsonify({'square': num ** 2})


# To-Do App
todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        if todo_id in todos:
            return {todo_id: todos[todo_id]}
        else:
            return '%s not available' % todo_id

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        if todo_id in todos:
            del todos[todo_id]
            return '%s deleted successfully!!!' % todo_id
        else:
            return "%s not available to be deleted." % todo_id


# # adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(TodoSimple, '/todo/<string:todo_id>')

# driver function
if __name__ == '__main__':
    app.run(debug=True)
