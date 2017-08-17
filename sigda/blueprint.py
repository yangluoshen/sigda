
from flask import Flask

_has_setup = False

def setup_blueprint(app: Flask):
    
    global _has_setup

    if _has_setup:
        return
    
    _has_setup = True
    
    from sigda.index.views import blueprint
    app.register_blueprint(blueprint, url_prefix='/index/')
