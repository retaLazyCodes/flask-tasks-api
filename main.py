from flask import Flask
from user import bp as user_bp
from task import bp as task_bp

app = Flask(__name__)
app.config['DEBUG'] = True
app.register_blueprint(user_bp)
app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(port=8000)
