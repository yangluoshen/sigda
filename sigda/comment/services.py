#coding:utf-8

from sigda.models import db, Comment
from sigda.config.common import ErrorCode
import logging


class CommentDbService(object):

    @staticmethod
    def add(contextid, userid, content, respto=None):

        logging.debug('db add comment {} {} {} {}'.format(contextid, userid, content, respto))

        c = Comment(contextid=contextid, userid=userid, content=content, respto=respto)

        db.session.add(c)
        try:
            db.session.flush()
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            logging.error('add comment')
            return None

        return c

    @staticmethod
    def delete(commentid):

        c = Comment.query.filter(Comment.id == commentid).first()

        if not c:
            return

        db.session.delete(c)
        db.session.commit()


