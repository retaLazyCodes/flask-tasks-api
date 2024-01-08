from flask_restx import fields

user_model = {
    'id': fields.Integer(required=True, description='ID del usuario'),
    'username': fields.String(required=True, description='Nombre de usuario'),
    'email': fields.String(description='Correo electrónico del usuario'),
    'password': fields.String(description='Contraseña del usuario', write_only=True)
}