#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Editor
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


class Producto:
	@property
	def forma(self):
		return self._forma
	@forme.setter
	def forma(self, forma):
		self._forma = forma
	@property
	def color(self):
		return self._color
	@color.setter
	def color(self, color):
		self._color = color
	def __str__(self):
		return 'Producto forma=%s color=%s' % (self.forma, self.color)

class Editor:
	@property
	def producto(self):
		return self._producto
	@producto.setter
	def producto(self, producto):
		self._producto = producto
	def crearProducto(self):
		self.producto = Producto()
	@abc.abstractmethod
	def diseniarForma(self):
		return
	@abc.abstractmethod
	def diseniarColor(self):
		return

class EditorCuboAzul(Editor):
	def diseniarForma(self):
		self.producto.forma = "Cubo"
	def diseniarColor(self):
		self.producto.color = "Azul"

class EditorEsferaRoja(Editor):
	def diseniarForma(self):
		self.producto.forma = "Esfera"
	def diseniarColor(self):
		self.producto.color = "Roja"

class EditorPiramideAmarilla(Editor):
	def diseniarForma(self):
		self.producto.forma = "Piramide"
	def diseniarColor(self):
		self.producto.color = "Amarilla"

class Director:
	@property
	def editor(self):
		return self._editor
	@editor.setter
	def editor(self, editor):
		self._editor = editor
	def diseniarProducto(self):
		self.editor.crearProducto()
		self.editor.diseniarForma()
		self.editor.diseniarColor()
		return self.editor.producto

director = Director()
director.editor = EditorPiramideAmarilla()
producto = director.diseniarProducto()
print(producto)

