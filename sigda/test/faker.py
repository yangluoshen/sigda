#coding:utf-8

import sys
sys.path.append('./')

import requests
import logging
from datetime import datetime
import json

logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(levelname) %(filename)s [line:%(lineno)d][%(funcName)s] %(message)s',  
                    datefmt='%m-%d %H:%M',  
                    filename='sida_test.log',  
                    filemode='a') 

host = '0.0.0.0'
port = '5757'


class Faker(object):


    def __init__(self, name=None):

        self.name = name or Faker.get_rand_fakername()
        self.email = 'faker@byted.com'

    @staticmethod
    def get_rand_fakername():
        
        import random
        faker_pool = ['Rengar', 'Fizz', 'Zed']
        return faker_pool[random.randint(0, len(faker_pool)-1)]



def log(func):

    def wrapper(*args, **kwargs):
        
        ret = func(*args, **kwargs)
        logging.debug(ret)

        return ret

    return wrapper

        
@log
def visit_index():
    
    return requests.get(url='http://{ip}:{port}/index/'.format(ip=host, port=port))

@log
def comment(contextid, name, content):

    data = {'contextid':contextid,
            'username': name,
            'content': content,
            }

    return requests.post(url='http://{ip}:{port}/comment/'.format(ip=host, port=port), data=data)


@log
def create_user(name, email):

    data = {'name': name, 'email': email}

    return requests.post(url='http://{ip}:{port}/user/'.format(ip=host, port=port), data=data)

@log
def create_context(creator, date, forwhom, details):

    data = {'creator': creator,
            'date': date,
            'forwhom': forwhom,
            'details': details,
            }

    return requests.post(url='http://{ip}:{port}/context/'.format(ip=host, port=port), data=data)

def testcase1():
    faker = Faker()

    rsp = create_user('shenweimin', faker.email)
    print(rsp.text)
    rsp = create_context('shenweimin', datetime.now().strftime("%m-%d"), 'Devil', 'Birthday')
    print(rsp.text)
    rsp = create_user('rengar', faker.email)
    print(rsp.text)
    rsp = comment('1', 'rengar', 'Happy birthday')
    print(rsp.text)


if __name__ == '__main__':

    testcase1()


    #visit_index()

    #rsp = comment('Happy Birthday!')

