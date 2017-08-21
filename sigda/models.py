# coding:utf-8

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import (BIGINT, DATETIME, INTEGER, VARCHAR)
from datetime import datetime

from sigda.config.common import USERNAME_LEN


db = SQLAlchemy()

class MySqlTableArgs(object):
    __table_args__ = {
        'mysql_engine' : 'InnoDB',
        'mysql_charset' : 'utf8mb4',
    }

class Comment(db.Model, MySqlTableArgs):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, nullable=False) #User.id
    contextid = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(1024), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    respto = db.Column(db.String(USERNAME_LEN), nullable=True)  

    def __init__(self, contextid, userid, content, respto):

        self.contextid = contextid
        self.userid = userid
        self.content = content
        self.time = datetime.now().strftime('%m-%d %H-%M')
        self.respto = respto

    def __repr__(self):

        return 'Comment({}, {},{},{})'.format(self.contextid, self.userid, self.content, self.respto)

    def __str__(self):

        return '<Comment {}, {}, {}, {}, {}>'.format(self.contextid, self.userid, self.content, self.time, self.respto)


class User(db.Model, MySqlTableArgs):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(USERNAME_LEN), nullable=False)
    email = db.Column(db.String(50), nullable=True)

    def __init__(self, name, email=''):

        self.name = name 
        self.email = email

    def __repr__(self):

        return 'User({}, {})'.format(self.name, self.email)

    def __str__(self):
        
        return repr(self)


'''
We may owe many significant days,
a `Context` indicate a significant day
'''
class Context(db.Model, MySqlTableArgs):
    __tablename__ = 'context'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator = db.Column(db.Integer, nullable=False) #User.id
    date = db.Column(db.String(20), nullable=False)
    forwhom = db.Column(db.String(USERNAME_LEN), nullable=True)
    details = db.Column(db.String(256), nullable=True)

    def __init__(self, creator, date, forwhom='', details=''):

        self.creator = creator
        self.date = date
        self.forwhom = forwhom
        self.details = details

    def __repr__(self):

        return 'Context({}, {}, {}, {})'.format(self.creator, self.date, self.forwhom, self.details)

    def __str__(self):

        return repr(self)



