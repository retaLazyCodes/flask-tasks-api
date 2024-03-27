from db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(256), unique=False, nullable=False)
    done = db.Column(db.Boolean, unique=False, default=False)