# -*- coding: utf-8 -*-
from flask import Blueprint

home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/')
def hi():
    return 'Hi Home!'

@home_bp.route('/bye')
def bye():
    return 'Bye bye Home!'