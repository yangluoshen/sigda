#coding:utf-8

from wtforms import (Form, StringField, DateTimeField)

class UserForm(Form):

    name = StringField('name')
    passwd = StringField('passwd')
    email = StringField('email')


