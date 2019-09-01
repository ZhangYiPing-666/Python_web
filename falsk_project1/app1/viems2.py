from flask import Blueprint

blue = Blueprint('viems2', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'

