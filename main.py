from flask import Flask
from flask_restx import Api
from namespaces.user import auth_ns
from namespaces.task import tasks_ns


app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title='My Tasks API',
    doc='/docs',
    prefix='/api'
)


def init():
    api.add_namespace(auth_ns)
    api.add_namespace(tasks_ns)
    app.run(port=8000, debug=True)


if __name__ == '__main__':
    init()


