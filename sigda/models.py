# coding:utf-8

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.dialects.mysql import (BIGINT, DATETIME, INTEGER, VARCHAR)
from datetime import datetime

db = SQLAlchemy()

class MySqlTableArgs(object):
    __table_agrs__ = {
        'mysql_engine' : 'InnoDB',
        'mysql_charset' : 'utf8mb4',
    }

class Comment(db.Model, MySqlTableArgs):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(1024), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    respto = db.Column(db.String(20), nullable=True)  #response to someone(userid)?

    def __init__(self, userid, content, respto):

        self.userid = userid
        self.content = content
        self.time = datetime.now().strftime('%m-%d %H-%M')
        self.respto = respto

    def __repr__(self):

        return 'Comment({},{},{})'.format(self.userid, self.content, self.respto)

    def __str__(self):

        return '<Comment {}, {}, {}, {}>'.format(self.userid, self.content, self.time, self.respto)


class User(db.Model, MySqlTableArgs):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)

    def __init__(self, name):

        self.name = name 

    def __repr__(self):

        return 'User({})'.format(self.name)

    def __str__(self):
        
        return '<User {},{}>'.format(self.id, self.name)


