from flask import Flask
from flask_script import Manager
from app1.viems1 import blue as blue_v1
from app1.viems2 import blue as blue_v2

app = Flask(__name__)

app.config["SECRET_KEY"] = "46164ASD4F61A6D45SF16A2SD41F65ASD1F"
app.register_blueprint(blueprint=blue_v1)
app.register_blueprint(blueprint=blue_v2)
manage = Manager(app=app)


if __name__ == '__main__':
    manage.run()
