# coding: utf-8

import sys,os
sys.path.append("./")

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from sigda.flaskapp import app
from sigda.models import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

