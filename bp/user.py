from flask import Blueprint
from flask_restx import Namespace
from controllers.user import Login, Logout, Register

user_bp = Blueprint('user', __name__)

auth_namespace = Namespace('auth', description='User authentication')
auth_namespace.add_resource(Login, '/login')
auth_namespace.add_resource(Logout, '/logout')
auth_namespace.add_resource(Register, '/register')
