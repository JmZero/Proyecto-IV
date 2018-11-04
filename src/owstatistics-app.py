#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import infojugador

app = Flask(__name__)

@app.route('/')
def inicio():
	return jsonify(status="Ok")

@app.route('/player/<battletag>')
def Info(battletag):
	p=funciones.InfoJugador()
	datos=p.isPerfilPublico(battletag)
	return jsonify(status="Ok")

@app.errorhandler(404)
def page_not_found(error):
    return 'Error HTTP 404, Not Found'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
