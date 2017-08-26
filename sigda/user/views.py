#coding:utf-8

from flask import Blueprint, request
from flask import render_template
import flask_login
import json
import logging

from sigda.config.response import JsonResponse
from sigda.config.common import ErrorCode
from sigda.user.forms import UserForm
from sigda.user.services import UserDbService, UserAuth

blueprint = Blueprint(__name__, __name__)

@blueprint.route('login/', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html', notifier='')

    logging.debug('%r'%request.form)
    form = UserForm(request.form)
    if not form.validate():
        logging.error('Invalid request')
        return render_template('login.html', notifier='输入有误')

    name = form.name.data
    email = form.email.data
    passwd = form.passwd.data
    u = UserDbService.get_user_by_email(email)
    if not u:

        user, code = UserDbService.add(name=name, email=email, passwd=passwd)
        if code == ErrorCode.EXIST:
            logging.error('user {} already exists.'.format(name))
            return render_template('login.html', notifier='昵称已经被存在')
        elif code == ErrorCode.FAILURE:
            logging.error('add user({}) failed'.format(name))
            return render_template('login.html', notifier='输入有误,请重试')
    else :
        if not UserDbService.auth(u):
            logging.debug('{} auth failed'.format(email))
            return render_template('login.html', notifier='密码有误')
        
    user_auth = UserAuth()
    user_auth.id = email
    flask_login.login_user(user_auth)
    logging.debug('create user success')
    return 'Welcome, {}.'.format(form.name.data)


@blueprint.route('logout/', methods=['GET', 'POST'])
def logout():
    flask_login.logout_user()
    return '已登出'

