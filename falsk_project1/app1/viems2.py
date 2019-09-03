# -*- coding: utf-8 -*-


from __future__ import unicode_literals  # 头部加上这句

from flask import Blueprint, render_template

blue = Blueprint('viems2', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/index/')
def index():
    return render_template("index.html")


@blue.route('/mine/')
def mine():
    return render_template("mine.html")



