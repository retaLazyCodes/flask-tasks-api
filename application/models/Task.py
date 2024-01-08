from flask_restx import fields

task_model = {
    'id': fields.Integer(required=True, description='ID de la tarea'),
    'title': fields.String(required=True, description='Título de la tarea'),
    'description': fields.String(description='Descripción de la tarea'),
    'done': fields.Boolean(description='Estado de finalización de la tarea')
}