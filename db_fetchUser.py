#!/user/bin/python
#-*- coding:utf-8 -*-
#author wanghaibo

from app import db, models
import datetime

# users = models.User.query.all()
# for u in users:
#     print(u.id,u.nickname)

#u = models.User.query.get(1)

u = models.User.query.get(1)
p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
db.session.commit()