#coding:utf-8

from flask import request
from flask_restful import Resource

from sigda.config.response import JsonResponse
from sigda.config.common import ErrorCode
from sigda.context.forms import ContextForm
from sigda.context.services import ContextDbService
from sigda.user.services import UserDbService

import logging

class CreateContext(Resource):

    def post(self):

        logging.debug('%r'%request.form)
        form = ContextForm(request.form)
        if not form.validate():
            logging.error('Invalid form')
            return JsonResponse({}, ErrorCode.FAILURE, 'Invalid form')

        creator = form.creator.data
        user = UserDbService.get_user_by_name(creator)
        if not user:
            logging.error('creator {} not found'.format(creator))
            return JsonResponse({}, ErrorCode.FAILURE, 'creator not register yet.')

        cxt = ContextDbService.add(user.id, form.date.data, form.forwhom.data, form.details.data)
        if not cxt:
            logging.error('create context failed.')
            return JsonResponse({}, ErrorCode.FAILURE, 'create context failed')

        logging.debug('%r'%cxt)

        return JsonResponse({'contextid': cxt.id}, ErrorCode.SUCCESS, 'create context OK')


