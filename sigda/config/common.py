#coding:utf-8

import logging.config

'''
logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(levelname) %(filename)s [line:%(lineno)d][%(funcName)s] %(message)s',  
                    datefmt='%m-%d %H:%M',  
                    filename='sigda_server.log',  
                    filemode='a') 
'''

LOG_LEVEL = 'DEBUG'
def get_log_config(category):
    log_file = "{}.log".format(category)
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s %(levelname)s %(message)s'
            },
            'console': {
                'format': "%(asctime)s [%(thread)d] %(levelname)s %(funcName)s\t%(message)s"
            },
        },
        'handlers': {
            'graylog2': {
                'level': LOG_LEVEL,
                'formatter': 'default',
                'class': 'graypy.GELFHandler',
                #'host': '0.0.0.0',
                'host': 'sigda-graylog2',
                'port': 12201,
                'debugging_fields': False,
                'facility': category
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'formatter': 'console',
                'filename': log_file
            }
        },
        'root': {
            'handlers': ['graylog2', 'file'],
            'level': LOG_LEVEL
        }
    }

SERVER_LOG_CONFIG = get_log_config('sigda_server')
logging.config.dictConfig(SERVER_LOG_CONFIG)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{password}@{host}/{db}?charset=utf8mb4'.format(
            host='sigda-mysql',
            password='sigda',
            db='sigda'
        )

class ErrorCode(object):

    SUCCESS = (0, 'Success')
    FAILURE = (-1, 'Failure')
    EXIST = (-2, 'Exist')


USERNAME_LEN = 30
PASSWD_LEN = 50

