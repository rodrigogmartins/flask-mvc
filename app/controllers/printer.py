# -*- coding: utf-8 -*-
from app import app
from flask import render_template, request

@app.route('/')
def start():
    return render_template('printer/index.html')

@app.route('/print', methods=['GET', 'POST'])
def printer():
    if request.method == 'POST':
        from app.models.Printer import Printer
        nome = request.form['nome']
        printer = Printer()
        return printer.show_string(nome)

