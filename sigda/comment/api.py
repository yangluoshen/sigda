#coding:utf-8

from flask import request
from flask_restful import Resource

from sigda.config.response import JsonResponse
from sigda.config.common import ErrorCode
from sigda.comment.forms import CommentForm, UserForm
from sigda.comment.services import CommentDbService, UserDbService

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

        content = form.content.data
        respto = form.respto.data

        CommentDbService.add(username, content, respto)

        logging.debug('create comment success')
        return JsonResponse({'username':username, 'content':content, 'respto':respto})

class CreateUser(Resource):

    def post(self):

        logging.debug('%r'%request.form)
        form = UserForm(request.form)
        if not form.validate():
            logging.error('Invalid request')
            return JsonResponse({}, ErrorCode.FAILURE, form.errors)

        user = UserDbService.add(name=form.name.data, email=form.email.data)
        if not user:
            logging.error('add user({}) failed'.format(form.name.data))
            return JsonResponse({}, ErrorCode.FAILURE, 'create failed')

        logging.debug('create user success')
        return 'Welcome, {}.'.format(form.name.data)

