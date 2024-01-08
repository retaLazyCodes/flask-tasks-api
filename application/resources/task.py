from flask_restx import Resource


class TaskList(Resource):
    def get(self):
        return {'tasks': []}

    def post(self):
        return {'message': 'Nueva tarea agregada'}


class Task(Resource):
    def get(self, id):
        return {'task': {}}

    def put(self, id):
        return {'message': f'La tarea con id {id} ha sido actualizado exitosamente.'}

    def delete(self, id):
        return {'message': f'Tarea con id {id} eliminada'}