#coding:utf-8

from sigda.models import db, User
from sigda.config.common import ErrorCode
import logging

class UserDbService(object):

    @staticmethod
    def add(name, email=''):

        u = UserDbService.get_user_by_name(name)
        if u:
            return u, ErrorCode.EXIST
        
        u = User(name=name, email=email)
        db.session.add(u)

        try:
            db.session.flush()
            db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            logging.error('add user')
            return None, ErrorCode.FAILURE

        return u, ErrorCode.SUCCESS

    @staticmethod
    def get_user_by_name(name):

        u = User.query.filter(User.name == name).first()

        return u

    @staticmethod
    def get_user_by_id(uid):

        u = User.query.filter(User.id == uid).first()

        return u


