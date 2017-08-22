#coding:utf-8

import sys,os
sys.path.append("./")

from flask import Flask 
import sigda.blueprint as blueprint
import sigda.config.common as const
from redis import Redis


def create_app():
    
    from sigda.models import db
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = const.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    return app

redis = Redis(host='sigda-redis', port=6379)
app = create_app()

def setup_app(fapp: Flask):

    blueprint.setup_blueprint(app)



if __name__ == '__main__':

    setup_app(app)
    app.run(host='0.0.0.0', debug=True, port=5757)



