#coding:utf-8

from flask import Blueprint, request
from flask import render_template
import json
import logging

blueprint = Blueprint(__name__, __name__)

@blueprint.route('/')
def home():

    return render_template('login.html', notifier='')




