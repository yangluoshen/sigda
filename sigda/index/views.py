#coding:utf-8

from flask import Blueprint, request
from flask import render_template
import flask_login
import json
import logging

blueprint = Blueprint(__name__, __name__)

@blueprint.route('/')
@flask_login.login_required
def home():

    return 'welcome'
    #return render_template('login.html', notifier='')




