from flask import Blueprint

bp = Blueprint('task', __name__)

@bp.route('/tasks')
def tasks():
    # Código para mostrar todas las tareas de un usuario
    return 'Todas las tareas'

@bp.route('/task/add')
def add_task():
    # Código para agregar una nueva tarea
    return 'Nueva tarea agregada'

@bp.route('/task/<id>/delete')
def delete_task(id):
    # Código para eliminar una tarea específica
    return f'Tarea con id {id} eliminada'
