from flask_restx import Resource


class Login(Resource):
    def post(self):
        # Código para el inicio de sesión
        return {'message': 'Inicio de sesión exitoso'}


class Register(Resource):
    def post(self):
        # Código para el registro de usuario
        return {'message': 'Registro de usuario exitoso'}


class Logout(Resource):
    def post(self):
        # Código para cerrar la sesión del usuario
        return {'message': 'Cierre de sesión exitoso'}
