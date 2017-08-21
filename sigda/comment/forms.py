#coding:utf-8

from wtforms import (Form, StringField, DateTimeField)

class CommentForm(Form):

    contextid = StringField('contextid')
    username = StringField('username')
    content = StringField('content')
    respto = StringField('respto')

