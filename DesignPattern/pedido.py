#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Comando
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"



import abc


class Movil:
	def moverIzquierda(self):
		print('El móvil se mueve a la izquierda')
	def moverDerecha(self):
		print('El móvil se mueve a la derecha')

class Comando(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def ejecutar(self):
		return

class IzquierdaComando(Comando):
	def __init__(self, movil):
		self.movil = movil
	def ejecutar(self):
		self.movil.moverIzquierda()

class DerechaComando(Comando):
	def __init__(self, movil):
		self.movil = movil
	def ejecutar(self):
		self.movil.moverDerecha()

class Piloto:
	def __init__(self, cG, cD):
		self.comandoIzquierda = cG
		self.comandoDerecha = cD
	def ordenIzquierda(self):
		self.comandoIzquierda.ejecutar()
	def ordenDerecha(self):
		self.comandoDerecha.ejecutar()

movil = Movil()
comando_izquierda = IzquierdaComando(movil)
comando_derecha = DerechaComando(movil)
piloto = Piloto(comando_izquierda, comando_derecha)

piloto.ordenIzquierda()
piloto.ordenDerecha()

