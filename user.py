from flask import Blueprint

bp = Blueprint('user', __name__)

@bp.route('/register')
def register():
    # Código para registrar un nuevo usuario
    return 'Nuevo usuario registrado'

@bp.route('/login')
def login():
    # Código para el inicio de sesión de un usuario existente
    return 'Sesión iniciada'

@bp.route('/logout')
def logout():
    # Código para cerrar la sesión de un usuario
    return 'Sesión cerrada'
