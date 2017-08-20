
from flask import Flask
from flask_restful import Api


_has_setup = False

def setup_blueprint(app: Flask):
    
    global _has_setup
    if _has_setup:
        return
    _has_setup = True

    api = Api(app)
    
    from sigda.index.views import blueprint
    app.register_blueprint(blueprint, url_prefix='/index')

    from sigda.comment.api import CreateComment
    api.add_resource(CreateComment, '/comment/')


