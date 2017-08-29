#!/user/bin/python
#-*- coding:utf-8 -*-
#author wanghaibo

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views  #放在脚本结束，因为他总是完成的，避免循环引用
