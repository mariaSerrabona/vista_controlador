#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Decorador
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


def decorator(param):
	def wrapper(func):
		def wrapped(arg):
			result = func(arg)
			return result > param and result or param
		return wrapped
	return wrapper

@decorator(20)
def calcul(arg):
	return arg

calcul(40)
calcul(10)

