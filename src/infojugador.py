#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class InfoJugador:

	def __init__(self):
		with open('./resrc/jugadores.json', 'r') as f:
			self.ap = json.load(f)

	# Función que devolverá el status
	def status(self):
		return 'OK'

	# Función que devolverá el Id del jugador
	def getBattleTag(self, user):
		for i in self.ap:
			if i["battletag"] == user:
				return user
			else:
				return False

	# Función que devolverá si el perfil es publico o privado
	def isPerfilPublico(self, user):
		try:
			for i in self.ap:
				if i["battletag"] == user:
					return i["perfil"]
				else:
					return False
		except:
			return False

	# Función que devolverá el nivel del jugador
	def getNivel(self, user):
		for i in self.ap:
			if i["battletag"] == user:
				return i["nivel"]
			else:
				return False

	# Función que devolverá el top 5 de personajes mas jugador por el jugador
	def getTop5(self, user):
		for i in self.ap:
			if i["battletag"] == user and i["perfil"] != "Privado":
				return i["top5"]
			else:
				return False

	# Función que añadirá un nuevo jugador
	def setJugador(self, user, perfil):
		try:
			self.ap.append({"battletag":user, "perfil":perfil})
			with open('./resrc/jugadores.json', 'w') as f:
				json.dump(self.ap, f)
			return True
		except:
			return False
