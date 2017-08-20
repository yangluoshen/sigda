#coding:utf-8
from wtforms import (Form, StringField, DateTimeField)

class CommentForm(Form):

    username = StringField('username')
    content = StringField('content')
    respto = StringField('respto')

class UserForm(Form):

    name = StringField('name')
    email = StringField('email')

