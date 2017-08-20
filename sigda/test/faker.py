#coding:utf-8

import sys
sys.path.append('./')

import requests
import logging
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
def comment(content):

    faker = Faker()
    data = {'username': faker.name,
            'content': content,
            }

    return requests.post(url='http://{ip}:{port}/comment/'.format(ip=host, port=port), data=json.dumps(data))


if __name__ == '__main__':

    visit_index()

    comment('Happy Birthday!')

