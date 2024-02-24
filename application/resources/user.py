from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import users

bp = Blueprint("Users", "users", description="Operations on users")

class Login(MethodView):
    def post(self):
        return {'message': 'Inicio de sesión exitoso'}


class Register(MethodView):
    def post(self):
        return {'message': 'Registro de usuario exitoso'}


class Logout(MethodView):
    def post(self):
        return {'message': 'Cierre de sesión exitoso'}
