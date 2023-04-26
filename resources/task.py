from flask_restx import Resource


class TaskList(Resource):
    def get(self):
        # Código para obtener todas las tareas de un usuario
        return {'tasks': []}

    def post(self):
        # Código para agregar una nueva tarea
        return {'message': 'Nueva tarea agregada'}


class Task(Resource):
    def get(self, id):
        # obtener una tarea por ID
        return {'task': {}}

    def put(self, id):
        # actualizar una tarea por ID
        return {'message': f'La tarea con id {id} ha sido actualizado exitosamente.'}

    def delete(self, id):
        # Código para eliminar una tarea específica
        return {'message': f'Tarea con id {id} eliminada'}