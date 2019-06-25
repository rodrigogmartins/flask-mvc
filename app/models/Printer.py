# -*- coding: utf-8 -*-
class Printer(object):

    def show_string(self, text):
        if text == '':
            return "Nenhum nome informado"
        else:
            return "Olá "+text+"!"
