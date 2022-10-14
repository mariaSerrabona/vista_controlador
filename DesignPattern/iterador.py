#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Iterador
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

class Iterador:
	def __init__(self, context):
		self.context = context.childs()
	def __iter__(self):
		return self
	def __next__(self):
		if len(self.context) == 0:
			raise StopIteration
		return self.context.pop(0)

class Componente(metaclass=abc.ABCMeta):
	def __init__(self, name):
		self.name = name
	@abc.abstractmethod
	def verbose(self, level=0):
		return
	def __iter__(self):
		return Iterador(self)

class Hoja(Componente):
	def verbose(self, level=0):
		return '%sHoja %s' % ('\t' * level, self.name)
	def childs(self):
		return [self]

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
	def childs(self):
		result = [self]
		for f in self.contenido:
			result.extend(f.childs())
		return result

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


for a in main:
	print(a.name)

