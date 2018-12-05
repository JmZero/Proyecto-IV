#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import json
import sys
sys.path.append('./src/')
import infojugador

app = Flask(__name__)

@app.route('/')
@app.route('/status')
def inicio():
	p=infojugador.InfoJugador()
	status=p.status()

	if status == 'OK':
		with open('status.json') as f:
			salida = json.load(f)
	return salida

@app.route('/player/<battletag>')
def info(battletag):
	p=infojugador.InfoJugador()
	perfil=p.isPerfilPublico(battletag)
	nivel=p.getNivel(battletag)

	if perfil == False:
		perfil = 'Privado'
		return jsonify(perfil=perfil, nivel=nivel)
	else:
		top5=p.getTop5(battletag)
		return jsonify(perfil=perfil, nivel=nivel, top5_personajes=top5)

@app.route('/player/<battletag>/top5')
def showTop5(battletag):
	p=infojugador.InfoJugador()
	perfil=p.isPerfilPublico(battletag)

	if perfil != False:
		top5=p.getTop5(battletag)
		return jsonify(top5_personajes=top5)
	else:
		return 'Este perfil es privado, no se pude obtener información'

@app.errorhandler(404)
def page_not_found(error):
    return 'Error HTTP 404, Not Found'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
