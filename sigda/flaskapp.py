#coding:utf-8

import sys,os
sys.path.append("./")

from flask import Flask 
import sigda.blueprint as blueprint

def create_app():
    
    app = Flask(__name__)

    return app

app = create_app()

def setup_app(fapp):

    blueprint.setup_blueprint(fapp)

if __name__ == '__main__':

    setup_app(app)
    app.run(host='0.0.0.0', debug=True, port=5757)



