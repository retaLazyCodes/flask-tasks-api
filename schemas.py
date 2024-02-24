from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    done = fields.Bool(required=True)

class TaskUpdateSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    done = fields.Bool()
