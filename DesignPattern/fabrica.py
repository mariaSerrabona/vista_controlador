#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Factoria
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
import os.path


class Loader(metaclass=abc.ABCMeta):
	def __new__(cls, filename):
		ext = os.path.splitext(filename)[-1]
		for sub in cls.__subclasses__():
			if sub.isDesignedFor(ext):
				o = object.__new__(sub)
				o.__init__(filename)
				return o
	def __init__(self, filename):
		self.filename = filename
	@classmethod
	def isDesignedFor(cls, ext):
		if ext in cls.extensions:
			return True
		return False
	@abc.abstractmethod
	def load(self):
		return

class TextLoader(Loader):
	extensions = ['.txt']
	def load(self):
		print('Archivo textual')
#		with open(self.filename) as f:
#			return f.readlines()

import csv
class CSVLoader(Loader):
	extensions = ['.csv']
	def load(self):
		print('Archivo CSV')
#		with open(self.filename) as f:
#			return cvs.reader(f.read())

import pickle
class PickleLoader(Loader):
	extensions = ['.pkl']
	def load(self):
		print('Archivo Pickle')
#		with open(self.filename) as f:
#			return pickle.load(f)


loader = Loader('archivo.txt')
type(loader)

