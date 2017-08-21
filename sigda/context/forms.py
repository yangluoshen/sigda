#coding:utf-8

from wtforms import (Form, StringField, DateTimeField)

class ContextForm(Form):

    creator = StringField('creator')
    date = StringField('date')
    forwhom = StringField('forwhom')
    details = StringField('details')





