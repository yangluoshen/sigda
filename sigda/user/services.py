#coding:utf-8

import flask_login
from flask import render_template

from sigda.models import db, User
from sigda.config.common import ErrorCode
import logging

login_manager = flask_login.LoginManager()

class UserDbService(object):

    @staticmethod
    def add(email, name,  passwd):

        u = UserDbService.get_user_by_email(email)
        if u:
            return u, ErrorCode.EXIST
        
        u = User(email=email, name=name, passwd=passwd)
        db.session.add(u)

        try:
            db.session.flush()
            db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            logging.error('add user')
            return None, ErrorCode.FAILURE

        return u, ErrorCode.SUCCESS

    @staticmethod
    def get_user_by_name(name):

        u = User.query.filter(User.name == name).first()

        return u

    @staticmethod
    def get_user_by_id(uid):

        u = User.query.filter(User.id == uid).first()

        return u

    @staticmethod
    def get_user_by_email(email):

        u = User.query.filter(User.email == email).first()

        return u

    @staticmethod
    def auth(user):

        if not user:
            return False

        real_user = UserDbService.get_user_by_email(user.email)
        if not real_user:
            return False

        return real_user.passwd == user.passwd


class UserAuth(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):

    u = UserDbService.get_user_by_email(email)
    if not u :
        return

    ua = UserAuth()
    ua.id = email
    return ua

@login_manager.request_loader
def request_loader(request):

    email = request.form.get('email')
    u = UserDbService.get_user_by_email(email)
    if not u:
        return

    ua = UserAuth()
    user.id = email
    
    user.is_authenticated = request.form['passwd'] == u.passwd

    return ua

@login_manager.unauthorized_handler
def unauthorized_handler():

    return render_template('login.html', notifier='')


