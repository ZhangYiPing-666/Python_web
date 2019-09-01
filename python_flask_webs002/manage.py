from flask import Flask
from flask_script import Manager
from app1.viems import blue

app = Flask(__name__)
app.register_blueprint(blueprint=blue)  # 注册蓝图
manage = Manager(app=app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manage.run()
