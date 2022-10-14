#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Flyweight
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


class A:
	def __init__(self, name):
		self.name = name
	def sayHello(self):
		return 'Hello %s' % self.name

class B:
	def sayHello(self, name):
		return 'Hello %s' % name

class C:
	@classmethod
	def sayHello(cls, name):
		return 'Hello %s' % name

class D:
	def sayHello(name):
		return 'Hello %s' % name

a = A('World')
a.sayHello()

b = B()
b.sayHello('World')

C.sayHello('World')

D.sayHello('World')

