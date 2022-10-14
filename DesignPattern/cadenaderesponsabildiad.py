#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Cadena de responsabilidad
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


class Componente:
	def __init__(self, name, condiciones):
		self.name = name
		self.condiciones = condiciones
		self.next = None
	def setNext(self, next):
		self.next = next
	def tratamiento(self, condition, message):
		if condition in self.condiciones:
			print('Tratramiento del mensaje %s por %s' % (message, self.name))
		if self.next is not None:
			self.next.tratamiento(condition, message)

c0 = Componente('c0', [1, 2])
c1 = Componente('c1', [1])
c2 = Componente('c2', [2])

c0.setNext(c1)
c1.setNext(c2)

c0.tratamiento(1, 'Test 1')
c0.tratamiento(2, 'Test 2')


