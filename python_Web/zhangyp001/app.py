#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import request
import requests as req
from test001 import res_dsqz_webservice

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p>url: <input name="url" value='http://172.25.2.106:52087/fpt-dsqz/services/DZFPService?wsdl' style="width:500px;height:30px"></p>
              <p>interfaceCode: <input interfaceCode="url" style="width:100px;height:30px"></p>
              <p>appid: <input appid="url" style="width:600px;height:30px"></p>
              <p>Key: <input Key="url" style="width:260px;height:30px"></p>
              <p>request_data: <textarea name="request_data" style="width:1000px;height:300px"></textarea></p>
              <p><button type="submit">Sign In</button></p>
              """<textarea style="width:700px;height:300px"></textarea>"""
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    url = request.form['url']
    request_data = request.form['request_data']
    res = res_dsqz_webservice(url, request_data)
    return '''<form action="/signin" method="post">
              <p>url: <textarea name="url" value='http://172.25.2.106:52087/fpt-dsqz/services/DZFPService?wsdl' style="width:500px;height:30px">{}</textarea></p>
              <p>request_data: <textarea name="request_data" style="width:1000px;height:300px">{}</textarea></p>
              <p><button type="submit">Sign In</button></p>
              """<textarea style="width:700px;height:300px">{}</textarea>"""
              </form>'''.format(url, request_data, res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8986, debug=True)
