import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import tasks

bp = Blueprint("Tasks", "tasks", description="Operations on tasks")


@bp.route("/task/<string:task_id>")
class Task(MethodView):
    def get(self, task_id):
        try:
            task = list(filter(lambda task: task["id"] == task_id, tasks))
            return {"task": task}
        except KeyError:
            abort(404, message="task not found.")

    def delete(self, task_id):
        try:
            tasks = [task for task in tasks if task["id"] != task_id]
            return {"message": "task deleted."}
        except KeyError:
            abort(404, message="task not found.")

    def put(self, task_id):
        task_data = request.get_json()
        if (
                "title" not in task_data or
                "description" not in task_data
            ):
            abort(
                400,
                message="Bad request. Ensure 'title' and 'description' are included in the JSON payload.",
            )
        if "done" not in task_data:
            task_data["done"] = False
        try:
            task = list(filter(lambda task: task["id"] == task_id, tasks))[0]
            task |= task_data
            return {'task': task}
        except KeyError:
            abort(404, message="Item not found.")


@bp.route("/task")
class TaskList(MethodView):
    def get(self):
        return {"tasks": tasks}

    def post(self):
        task_data = request.get_json()
        if (
                "title" not in task_data or
                "description" not in task_data
            ):
            abort(
                400,
                message="Bad request. Ensure 'title' and 'description' are included in the JSON payload.",
            )
        if "done" not in task_data:
            task_data["done"] = False
        task_id = uuid.uuid4().hex
        task = {**task_data, "id": task_id}
        tasks.append(task)
        return {'task': task}