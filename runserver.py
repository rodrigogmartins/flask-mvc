#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import app
from flask import Blueprint
from app.controllers.blueprints.exemplo.hello_bp import cobaia_bp

app.register_blueprint(cobaia_bp)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run('0.0.0.0', port=port)


