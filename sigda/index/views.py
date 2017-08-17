#coding:utf-8

from flask import Blueprint, request
import json
import logging

blueprint = Blueprint(__name__, __name__)

@blueprint.route('/')
def home():

    return 'Hello Sigda'


