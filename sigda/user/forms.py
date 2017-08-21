#coding:utf-8

from wtforms import (Form, StringField, DateTimeField)

class UserForm(Form):

    contextid = StringField('contextid')
    name = StringField('name')
    email = StringField('email')


