#coding:utf-8

from sigda.models import db, Comment, User
import logging


class CommentDbService(object):

    @staticmethod
    def add(userid, content, respto=None):

        logging.debug('db add comment {} {} {}'.format(userid, content, respto))

        c = Comment(userid=userid, content=content, respto=respto)

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


class UserDbService(object):

    @staticmethod
    def add(name, email=''):

        u = User(name=name, email=email)
        db.session.add(u)

        try:
            db.session.flush()
            db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            logging.error('add user')
            return None

        return u

    @staticmethod
    def get_user_by_name(name):

        u = User.query.filter(User.name == name).first()

        return u

    @staticmethod
    def get_user_by_id(uid):

        u = User.query.filter(User.id == uid).first()

        return u

