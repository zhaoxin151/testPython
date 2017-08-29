#!/user/bin/python
#-*- coding:utf-8 -*-
#author wanghaibo

import os

WTF_CSRF_ENABLED = True   #激活跨站点请求伪造
SECRET_KEY = 'you-will-never-guess'  #仅当启用CSRF时才需要该设置

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  #SQLALCHEMY_DATABASE_URI是Flask-SQLAlchemy扩展所必需的。这是我们的数据库文件的路径。
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')   #SQLALCHEMY_MIGRATE_REPO是我们将存储SQLAlchemy-migrate数据文件的文件夹。

