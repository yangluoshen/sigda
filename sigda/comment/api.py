#coding:utf-8

from flask import request
from flask_restful import Resource

from sigda.config.response import JsonResponse
from sigda.config.common import ErrorCode
from sigda.comment.forms import CommentForm
from sigda.comment.services import CommentDbService
from sigda.user.services import UserDbService

import logging

class CreateComment(Resource):

    def post(self):
        
        logging.debug('%r'%request.form)
        form = CommentForm(request.form)
        if not form.validate():
            logging.error('Invalid request')
            return JsonResponse({}, ErrorCode.FAILURE, form.errors)

        username = form.username.data 
        user = UserDbService.get_user_by_name(username)
        if not user:
            logging.error('{} not found'.format(username))
            return JsonResponse({}, ErrorCode.FAILURE, 'user not found')

        contextid = int(form.contextid.data)
        content = form.content.data
        respto = form.respto.data


        comment = CommentDbService.add(contextid, user.id, content, respto)
        if not comment:
            logging.error('add comment failed')
            return JsonResponse({}, ErrorCode.FAILURE, 'add comment failed')

        logging.debug('create comment success')
        return JsonResponse({'username':username, 'content':content, 'respto':respto})

