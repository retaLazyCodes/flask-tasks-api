from flask_restx import Namespace
from resources.task import Task, TaskList

tasks_ns = Namespace('tasks', description='Tasks endpoints')
tasks_ns.add_resource(TaskList, '/')
tasks_ns.add_resource(Task, '/<int:id>')
