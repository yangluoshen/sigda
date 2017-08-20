
import logging

logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(levelname) %(filename)s [line:%(lineno)d][%(funcName)s] %(message)s',  
                    datefmt='%m-%d %H:%M',  
                    filename='sigda_server.log',  
                    filemode='a') 

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{password}@{host}/{db}?charset=utf8mb4'.format(
            host='sigda-mysql',
            password='sigda',
            db='sigda'
        )

class ErrorCode(object):

    SUCCESS = (0, 'Success')
    FAILURE = (-1, 'Failure')


USERNAME_LEN = 30

