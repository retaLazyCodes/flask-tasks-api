from flask_restx import Resource


class Login(Resource):
    def post(self):
        return {'message': 'Inicio de sesión exitoso'}


class Register(Resource):
    def post(self):
        return {'message': 'Registro de usuario exitoso'}


class Logout(Resource):
    def post(self):
        return {'message': 'Cierre de sesión exitoso'}
