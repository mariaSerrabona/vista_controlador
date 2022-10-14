#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Recuerdo
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


class Current:
	def __init__(self, state):
		class Recuerdo:
			state = None
		self.state = state
		self.recuerdo = Recuerdo()
	def setState(self, state):
		self.recuerdo.state, self.state = self.state, state
	def resetState(self):
		state = self.recuerdo.state
		if state is None:
			print("No es posible volver atrás")
		self.recuerdo.state, self.state = None, self.recuerdo.state

c = Current('1')
print(c.state)
c.setState('2')
print(c.state)
c.resetState()
print(c.state)
c.setState('3')
print(c.state)
c.resetState()
print(c.state)
c.resetState()

