#coding:utf-8

from flask import Blueprint, request
from flask import render_template
import json
import logging

from sigda.config.response import JsonResponse
from sigda.config.common import ErrorCode
from sigda.user.forms import UserForm
from sigda.user.services import UserDbService

blueprint = Blueprint(__name__, __name__)

@blueprint.route('login/', methods=['POST'])
def login():

    logging.debug('%r'%request.form)
    form = UserForm(request.form)
    if not form.validate():
        logging.error('Invalid request')
        return render_template('login.html', notifier='输入有误')

    user, code = UserDbService.add(name=form.name.data, email=form.email.data)
    if code == ErrorCode.EXIST:
        logging.error('user {} already exists.'.format(form.name.data))
        return render_template('login.html', notifier='昵称已经被存在')
    elif code == ErrorCode.FAILURE:
        logging.error('add user({}) failed'.format(form.name.data))
        return render_template('login.html', notifier='输入有误,请重试')

    logging.debug('create user success')
    return 'Welcome, {}.'.format(form.name.data)
    return render_template('login.html', notifier='')




