#coding:utf-8

from sigda.config.common import ErrorCode

class JsonResponse(dict):

    def __init__(self, data=None, error=ErrorCode.SUCCESS, msg=''):

        self.data = data or {}
        self.code, msg = error
        if msg:
            self.msg = msg

        super(JsonResponse, self).__init__(data=self.data, code=self.code, msg=self.msg)

if __name__ == '__main__': 

    jrsp = JsonResponse(data={'username':'Rengar', 'comment':'Happy Birthday'})

    print (jrsp)



