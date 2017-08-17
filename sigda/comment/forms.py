#coding:utf-8
from wtfroms import (Form, StingField, DateTimeField)

class GetCommentForm(Form):

    username = StringField('username')
    comment = StringField('comment')
