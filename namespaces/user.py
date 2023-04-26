from flask_restx import Namespace
from resources.user import Login, Logout, Register

auth_ns = Namespace('auth', description='User endpoints')
auth_ns.add_resource(Login, '/login')
auth_ns.add_resource(Logout, '/logout')
auth_ns.add_resource(Register, '/register')
