# coding: utf-8
from flask import Blueprint

cobaia_bp = Blueprint('cobaia', __name__)

@cobaia_bp.route('/hello')
def index():
    return 'Hello!'
