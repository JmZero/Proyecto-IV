#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import sys
sys.path.append('./src/')
import infojugador

app = Flask(__name__)

@app.route('/')
def inicio():
	return jsonify(status="Ok")

@app.route('/player/<battletag>')
def info(battletag):
	p=infojugador.InfoJugador()
	datos=p.isPerfilPublico(battletag)
	if datos == False:
		datos = 'Privado'
	return jsonify(perfil=datos)

@app.errorhandler(404)
def page_not_found(error):
    return 'Error HTTP 404, Not Found'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
