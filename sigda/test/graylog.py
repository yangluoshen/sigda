#coding:utf-8

#from graypy import GELFHandler

import logging.config
import logging

'''
handler = GELFHandler(host='0.0.0.0', port=12201)
logger = logging.getLogger()

logger.addHandler(handler)
logger.error('catch error')
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
                'host': '0.0.0.0',
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

LOG_CONFIG = get_log_config('sigda')
logging.config.dictConfig(LOG_CONFIG)

logging.error('catch error again2')





