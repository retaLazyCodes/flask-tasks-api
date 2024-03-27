import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from application.models import TaskModel
from schemas import TaskSchema, TaskUpdateSchema

bp = Blueprint("Tasks", "tasks", description="Operations on tasks")


@bp.route("/task/<string:task_id>")
class Task(MethodView):
    @bp.response(200, TaskSchema)
    def get(self, task_id):
        item = TaskModel.query.get_or_404(task_id)
        return item

    def delete(self, task_id):
        item = TaskModel.query.get_or_404(task_id)
        raise NotImplementedError("Deleting a taks is not implemented.")

    @bp.arguments(TaskUpdateSchema)
    @bp.response(200, TaskSchema)
    def put(self, task_data, task_id):
        item = TaskModel.query.get_or_404(task_id)
        raise NotImplementedError("Updating an item is not implemented.")


@bp.route("/task")
class TaskList(MethodView):
    @bp.response(200, TaskSchema(many=True))
    def get(self):
        return tasks

    @bp.arguments(TaskSchema)
    @bp.response(201, TaskSchema)
    def post(self, task_data):
        task = TaskModel(**task_data)
        
        try:
            db.session.add(task)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")
        
        return task