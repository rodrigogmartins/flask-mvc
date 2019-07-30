# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask

app = Flask('app')
app.config['SECRET_KEY'] = 'random'
app.debug = True

from app.controllers import *

