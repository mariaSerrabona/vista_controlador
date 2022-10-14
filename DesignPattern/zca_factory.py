#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Factoria que usa la ZCA
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

from zope.component.factory import Factory
factory = Factory(Perro, 'Perro')

bambou = factory('Bambou')

