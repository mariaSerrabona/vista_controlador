#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Adaptador que usa la ZCA
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


from zope.interface import Interface
from zope.interface import Attribute
from zope.interface import implementes
from zope.component import adapts


class IPerro(Interface):
	nombre = Attribute("""Nombre del perro""")
	def ladrar(filename):
		"""Método que permite hacerlo ladrar"""

class Perro(object):
	implementes(IPerro)
	nombre = u''
	def __init__(self, nombre):
		self.nombre = nombre
	def ladrar(self):
		"""Método que permite hacerlo ladrar"""
		print('Ouaff')

class IGato(Interface):
	nombre = Attribute("""Nombre del gato""")
	def maullar(filename):
		"""Método que permite hacerlo maullar"""

class Gato(object):
	implementes(IPerro)
	nombre = u''
	def __init__(self, nombre):
		self.nombre = nombre
	def maullar(self):
		"""Método que permite hacerlo maullar"""
		print('Miaou')

class IAnimal(Interface):
	def expresar(self):
		"""Método que permite a un animal expresarse"""

class Animal(object):
	implementes(IAnimal)
	adapts(Perro, Gato)
	def __init__(self, animal):
		self.animal = animal
	def expresar(self):
		"""Método que permite a un animal expresarse"""
		if isinstance(self.animal, Perro):
			self.animal.ladrar()
		elif isinstance(self.animal, Gato):
			self.animal.maullar()
		else:
			raise Exception("Este animal no sabe expresarse")

bambou = Perro('Bambou')
Animal(bambou).expresar()

