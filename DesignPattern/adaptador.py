#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Adaptador
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


class Perro:
	def ladrar(self):
		print('Ouaff')

class Gato:
	def maullar(self):
		print('Miaou')

class Caballo:
	def relinchar(self):
		print('Hiiii')

class Cerdo:
	def grunir(self):
		print('Gruik')


class Animal(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def pintarRuido(self):
		return

class PerroAlternativa(Animal, Perro):
	def pintarRuido(self):
		return self.ladrar()

class GatoAlternativa(Animal, Gato):
	pintarRuido = Gato.maullar

class CaballoAlternativa(Animal):
	def __init__(self, caballo):
		self.caballo = caballo
	def pintarRuido(self):
		return self.caballo.relinchar()
	def __getattr__(self, attr):
		return self.caballo.__getattr__(attr)

class CerdoAdaptador:
	def __init__(self, cerdo):
		self.cerdo = cerdo
	def __getattr__(self, attr):
		if attr == 'pintarRuido':
			return self.cerdo.grunir
		return getattr(self.cerdo, attr)

for animal in [PerroAlternativa(), GatoAlternativa(), CaballoAlternativa(Caballo()), CerdoAdaptador(Cerdo())]:
	animal.pintarRuido()


class PerroAdaptador:
	def __init__(self, perro):
		self.perro = perro
	def __getattr__(self, attr):
		if attr == 'pintarRuido':
			return self.perro.ladrar
		return getattr(self.perro, attr)

class GatoAdaptador:
	def __init__(self, gato):
		self.gato = gato
	def __getattr__(self, attr):
		if attr == 'pintarRuido':
			return self.gato.maullar
		return getattr(self.gato, attr)

class CaballoAdaptador:
	def __init__(self, caballo):
		self.caballo = caballo
	def __getattr__(self, attr):
		if attr == 'pintarRuido':
			return self.caballo.relinchar
		return getattr(self.caballo, attr)

def animal_adapterFactory(context):
	if isinstance(context, Perro):
		return PerroAdaptador(context)
	elif isinstance(context, Gato):
		return GatoAdaptador(context)
	elif isinstance(context, Caballo):
		return CaballoAdaptador(context)
	elif isinstance(context, Cerdo):
		return CerdoAdaptador(context)
	else:
		raise Exception('Adaptador no encontrado')

for animal in [Perro(), Gato(), Caballo(), Cerdo()]:
	animal_adapterFactory(animal).pintarRuido()

