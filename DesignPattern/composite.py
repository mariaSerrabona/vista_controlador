#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Composicion
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

class Componente(metaclass=abc.ABCMeta):
	def __init__(self, name):
		self.name = name
	@abc.abstractmethod
	def verbose(self, level=0):
		return

class Hoja(Componente):
	def verbose(self, level=0):
		return '%sHoja %s' % ('\t' * level, self.name)

class Composicion(Componente):
	def __init__(self, name):
		Componente.__init__(self, name)
		self.contenido = []
	def add(self, componente):
		self.contenido.append(componente)
	def verbose(self, level=0):
		hojas = [f.verbose(level+1) for f in self.contenido]
		hojas.insert(0, '%sComposición %s' % ('\t' * level, self.name))
		return '\n'.join(hojas)

c1 = Hoja('F1')
c2 = Hoja('F2')
c3 = Composicion('C1')
c3.add(Hoja('F4'))
c3.add(Hoja('F5'))
c3.add(Hoja('F6'))
c4 = Composicion('C2')
c41 = Composicion('C3')
c41.contenido = [Hoja('F7'), Hoja('F8'), Hoja('F9')]
c4.contenido = [Composicion('C4'), c41, Hoja('FA')]

main = Composicion('Test')
main.contenido.extend([c1, c2, c3, c4])

print(main.verbose())

