from flask import Blueprint
from flask_restx import Namespace
from controllers.task import Task, TaskList

task_bp = Blueprint('task', __name__)

tasks_namespace = Namespace('tasks', description='Tasks endpoints')
tasks_namespace.add_resource(TaskList, '/')
tasks_namespace.add_resource(Task, '/<int:id>')
