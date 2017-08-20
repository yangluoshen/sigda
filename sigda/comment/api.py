#coding:utf-8

from flask import request
from flask_restful import Resource

from sigda.config.response import JsonResponse
from sigda.config.common import ErrorCode
from sigda.comment.forms import CommentForm

import logging

class CreateComment(Resource):

    def post(self):
        
        logging.error("Enter")
        form = CommentForm(request.form)
        if not form.validate():
            logging.error('Invalid request')
            return JsonResponse({}, ErrorCode.Failure, form.errors)

        username = form.username.data 
        content = form.content.data
        respto = form.respto.data

        logging.debug(form)

        logging.debug('create comment')
        return JsonResponse({'username':username, 'content':content, 'respto':respto})

