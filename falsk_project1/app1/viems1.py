from flask import Blueprint, render_template, url_for, request, Response, redirect, session

blue = Blueprint('viems1', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/home/')
def home():
    # username = request.cookies.get("username")
    username = session.get("user")
    return render_template('home.html', username=username)


@blue.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get("username")
        session["user"] = username
        resp = Response("欢迎回来%s" % username)
        # resp.set_cookie(key='username', value=username)
        return resp


@blue.route('/logout/')
def logout():
    resp = redirect(url_for('viems1.home'))
    # resp.delete_cookie(key="username")
    return resp