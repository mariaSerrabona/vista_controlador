#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Proxy
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


class IdentityProxy:
	def __init__(self, context):
		self.context = context
	def __getattr__(self, name):
		return getattr(self.context, name)


class Point:
	def __init__(self, x, y ,z):
		self._x, self._y, self._z = x, y, z
	def x(self):
		return str(self._x)
	def y(self):
		return str(self._y)
	def z(self):
		return str(self._z)

class Projection(IdentityProxy):
	def z(self):
		return '0'

def formatter(point):
	return '(%s)' % ', '.join([point.x(), point.y(), point.z()])

point = Point(1, 2, 3)
projection = Projection(point)

print(formatter(point))
print(formatter(projection))

class A:
	def m1(self):
		pass
	def m2(self):
		pass

class ProxyDeA:
	def __init__(self):
		self.context = A()
	def m1(self):
		return self.context.m1(self)

class ProxySelectif:
	redirected = ['m1', 'm3']
	def __init__(self, context):
		self.context = context
	def __getattr__(self, name):
		if name in self.redirected:
			return getattr(self.context, name)


a1 = A()
'm1' in dir(a1), 'm2' in dir(a1)
a2 = ProxyDeA()
'm1' in dir(a2), 'm2' in dir(a2)

a3 = ProxySelectif(A())
'm1' in dir(a3), 'm2' in dir(a3)
a3.m1

