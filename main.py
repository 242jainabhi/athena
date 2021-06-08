from flask import Flask
from flask_restful import Api
from resources import health_check, hello, todo, square

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return 'Welcome to Athena'


api.add_resource(health_check.Health, '/health')
api.add_resource(hello.Hello, '/hello')
api.add_resource(square.Square, '/square/<int:num>')
api.add_resource(todo.TodoSimple, '/todo/<string:todo_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)

