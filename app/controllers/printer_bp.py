# -*- coding: utf-8 -*-
from flask import render_template, request
from flask import Blueprint

printer_bp = Blueprint('printer_BP', __name__, url_prefix='/printer')

@printer_bp.route('/')
def start():
    return render_template('printer/index.html')

@printer_bp.route('/print', methods=['GET', 'POST'])
def printer():
    if request.method == 'POST':
        from app.models.Printer import Printer
        
        nome = request.form['nome']
        printer = Printer()

        return printer.show_string(nome)

