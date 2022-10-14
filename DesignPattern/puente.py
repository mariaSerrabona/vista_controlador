#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Puente
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
class Loader(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def load(self):
		return

#import csv
class CSVLoader(Loader):
	def load(self, filename):
		print('Archivo CSV')
#		with open(filename) as f:
#			return cvs.reader(f.read())

#import pickle
class PickleLoader(Loader):
	def load(self, filename):
		print('Archivo Pickle')
#		with open(filename) as f:
#			return pickle.load(f)

class Transformer(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def transform(self):
		return

class UpperTransformer(Transformer):
	def __init__(self, filename, *args, loader):
		self.filename = filename
		self.loader = loader
	def loadDatas(self):
		self.content = self.loader.load(self.filename)
		# Cuando haya comentarios en el loader
		if self.content is None:
			self.content = [
				['Truc', 'machin'],
				['cHoSe', 'BIDULE']]
	def transform(self):
		for i, l in enumerate(self.content):
			for j, d in enumerate(l):
				self.content[i][j] = d.upper()

class LowerTransformer(Transformer):
	def __init__(self, filename, *args, loader):
		self.filename = filename
		self.loader = loader
	def loadDatas(self):
		self.content = self.loader.load(self.filename)
		# Cuando haya comentarios en el loader
		if self.content is None:
			self.content = [
				['Truc', 'machin'],
				['cHoSe', 'BIDULE']]
	def transform(self):
		for i, l in enumerate(self.content):
			for j, d in enumerate(l):
				self.content[i][j] = d.lower()

test1 = UpperTransformer('test.csv', loader=CSVLoader())
test1.loadDatas()
test1.transform()
test1.content

test2 = LowerTransformer('test.pkl', loader=PickleLoader())
test2.loadDatas()
test2.transform()
test2.content

