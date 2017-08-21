#coding:utf-8

from flask import request
from flask_restful import Resource

from sigda.config.response import JsonResponse
from sigda.config.common import ErrorCode
from sigda.user.forms import UserForm
from sigda.user.services import UserDbService

import logging


class CreateUser(Resource):

    def post(self):

        logging.debug('%r'%request.form)
        form = UserForm(request.form)
        if not form.validate():
            logging.error('Invalid request')
            return JsonResponse({}, ErrorCode.FAILURE, form.errors)

        user, code = UserDbService.add(name=form.name.data, email=form.email.data)
        if code == ErrorCode.EXIST:
            logging.error('user {} already exists.'.format(form.name.data))
            return JsonResponse({}, ErrorCode.EXIST, 'user {} already exists.'.format(form.name.data))
        elif code == ErrorCode.FAILURE:
            logging.error('add user({}) failed'.format(form.name.data))
            return JsonResponse({}, ErrorCode.FAILURE, 'create failed')

        logging.debug('create user success')
        return 'Welcome, {}.'.format(form.name.data)

