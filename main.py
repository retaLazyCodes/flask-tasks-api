from flask import Flask
from flask_restx import Api
from bp.user import user_bp, auth_namespace
from bp.task import task_bp, tasks_namespace


def register_blueprints_and_namespaces(app, api):
    app.register_blueprint(user_bp)
    app.register_blueprint(task_bp)
    api.add_namespace(auth_namespace)
    api.add_namespace(tasks_namespace)


app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title='My Tasks API',
    doc='/docs',
    prefix='/api'
)

register_blueprints_and_namespaces(app, api)

if __name__ == '__main__':
    app.run(port=8000, debug=True)


