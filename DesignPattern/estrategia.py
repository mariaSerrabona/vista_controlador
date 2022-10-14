#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Estrategia
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


strategy1 = lambda x: x.lower()
strategy2 = lambda x: x.upper()

class StrategyManager:
	def bind(self, func):
		self.execute = func

manager = StrategyManager()
manager.bind(strategy1)
manager.execute('Dato')
manager.bind(strategy2)
manager.execute('Dato')

