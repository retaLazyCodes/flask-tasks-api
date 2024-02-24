import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import tasks
from schemas import TaskSchema, TaskUpdateSchema

bp = Blueprint("Tasks", "tasks", description="Operations on tasks")


@bp.route("/task/<string:task_id>")
class Task(MethodView):
    @bp.response(200, TaskSchema)
    def get(self, task_id):
        try:
            task = list(filter(lambda task: task["id"] == task_id, tasks))
            if not task:
                abort(404, message="Task not found.")
            return task[0]
        except KeyError:
            abort(404, message="task not found.")

    def delete(self, task_id):
        global tasks
        try:
            tasks = [task for task in tasks if task["id"] != task_id]
            return {"message": "task deleted."}
        except KeyError:
            abort(404, message="task not found.")

    @bp.arguments(TaskUpdateSchema)
    @bp.response(200, TaskSchema)
    def put(self, task_data, task_id):
        global tasks
        try:
            task_index = next((index for index, task in enumerate(tasks) if task["id"] == task_id), None)
            if task_index is not None:
                tasks[task_index].update(task_data)
                return tasks[task_index], 200
            else:
                abort(404, message="Task not found.")
        except KeyError:
            abort(404, message="Task not found.")


@bp.route("/task")
class TaskList(MethodView):
    @bp.response(200, TaskSchema(many=True))
    def get(self):
        return tasks

    @bp.arguments(TaskSchema)
    @bp.response(201, TaskSchema)
    def post(self, task_data):
        task_id = uuid.uuid4().hex
        task = {**task_data, "id": task_id}
        tasks.append(task)
        return task