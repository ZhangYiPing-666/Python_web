from flask import Flask, make_response, Response, redirect, render_template, request, url_for, abort, json
from flask_script import Manager
import uuid


app = Flask(__name__)
manage = Manager(app)


@app.route('/')
def hello_world():
    return '肖尔娜是美女'


@app.route('/login/')
def login():
    return render_template("login.html/")


@app.route('/get_params/<argms>/')
def get_params(argms):
    return argms


@app.route('/get_params_pass/<path:argms>/')
def get_params_pass(argms):
    return argms


@app.route('/get_params1_uuid/<uuid:argms>/')
def get_params1_uuid(argms):
    return argms


@app.route('/get_uuid/')
def get_uuid():
    print(str(uuid.uuid4()))
    return str(uuid.uuid4())


@app.route('/get_any/<any(a, b, c):argms>')
def get_any(argms):
    return argms


@app.route("/req", methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def req():
    print(request.method)
    print(request.args)
    print(request.data)
    print(request.form)
    # print(request.files)
    print(request.cookies)
    print(request.remote_addr)
    print(request.user_agent)
    print(request.url)
    return 'req'


@app.route("/response", methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def res():
    # response = render_template("login.html")  # 字符串响应类型
    # response = make_response('<h1>响应</h1>', 200)  # 制作response响应类型
    response = Response(response='德玛西亚', status=200)  # 创建response响应类型
    return response


@app.route('/redirect/', methods=['GET'])
def re_to():
    response = redirect(url_for('login'))
    print(response)
    print(type(response))
    return response


@app.route('/abort/', methods=['GET'])
def abor_t():
    abort(405)


# 返回json格式的响应
@app.route('/json/', methods=['GET'])
def get_json():
    result = json.jsonify(name='zhangyp', age='25')
    # response = Response(response='{"name": "zhangyp"}', content_type='application/json', status=200)
    return result


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=1314, debug=True, threaded=4)
    manage.run()