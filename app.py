from flask import Flask
from flask_smorest import Api
from db import db
import os
import application.models
from application.resources.user import bp as UserBlueprint
from application.resources.task import bp as TaskBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Tasks REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "mssql+pymssql://sa:12345@localhost:1433/dbTest")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(TaskBlueprint)

    return app

if __name__ == "__main__":
    create_app().run(port=8000, debug=True)

