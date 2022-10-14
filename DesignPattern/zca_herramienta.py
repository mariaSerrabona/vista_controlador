#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Herramienta que usa la ZCA
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
from zope.interface import implementes


class IIdGenerator(Interface):
	def get(self):
		"""Proporciona un id único"""
	def getIdFor(self, category):
		"""Proporciona un id único para cada categoria"""

class IdGenerator(object):
	implementes(IIdGenerator)
	def __init__(self):
		self.id = 0
		self.ids = {}
	def get(self):
		"""Proporciona un id único"""
		self.id += 1
		return self.id
	def getIdFor(self, category):
		"""Proporciona un id único para cada categoria"""
		if category not in self.ids.keys():
			self.ids[category] = 0
		self.ids[category] += 1
		return self.ids[category]

id_generator = IdGenerator()

