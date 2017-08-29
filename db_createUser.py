#!/user/bin/python
#-*- coding:utf-8 -*-
#author wanghaibo

from app import db, models

u = models.User(nickname='susan', email='susan@email.com')
db.session.add(u)
db.session.commit()