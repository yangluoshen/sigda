#coding:utf-8

from sigda.models import db, Context
from sigda.config.common import ErrorCode
import traceback
import logging

class ContextDbService(object):

    @staticmethod
    def add(creator, date, forwhom, details=''):

        c = Context(creator, date, forwhom, details)
        db.session.add(c)

        try:
            db.session.flush()
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            logging.error('add context failed. {}'.format(traceback.format_exc()))
            return None

        return c


    @staticmethod
    def get_context_by_id(cid):

        c = Context.query.filter(Context.id == cid).first()

        return c


