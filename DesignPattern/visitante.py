#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Visitante
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


class Visitante1:
	def visitarCasilla(self, casilla):
		print('Visita la casilla')
	def visitarCirculo(self, circulo):
		print('Visita del circulo')

class Visitante2:
	def visitarCasilla(self, casilla):
		print(casilla.medida)
	def visitarCirculo(self, circulo):
		print(circulo.medida)

class Casilla:
	medida = 'longitud del lado'
	def accept(self, visitante):
		visitante.visitarCasilla(self)

class Circulo:
	medida = 'radio'
	def accept(self, visitante):
		visitante.visitarCirculo(self)

Casilla().accept(Visitante1())
Circulo().accept(Visitante2())

