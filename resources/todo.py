from flask_restful import Resource
from flask import request


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
