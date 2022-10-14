#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patrón de diseño Facade
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


class Word:
	def hello(self):
		return 'Hello, I\'m'
	def goodbye(self):
		return 'GoodBye, I\'m'

class Speaker:
	def __init__(self, name):
		self.name = name
	@classmethod
	def say(cls, what, to):
		word = Word()
		metodo = getattr(word, what)
		if metodo is None:
			return ''
		return ' '.join([metodo(), to])
	def speak(self, what):
		return Speaker.say(what, self.name)
	def who(self):
		return self.name

class Dialog:
	def __init__(self, speaker1, speaker2):
		self.speaker1 = Speaker(speaker1)
		self.speaker2 = Speaker(speaker2)
		self.sentences = []
	def __call__(self):
		sentences = []
		sentences.append(self.speaker1.speak('hello'))
		sentences.append(self.speaker2.speak('hello'))
		sentences.extend(self.sentences)
		sentences.append(self.speaker1.speak('goodbye'))
		sentences.append(self.speaker2.speak('goodbye'))
		return '\n'.join(['- %s' % s for s in sentences])

class Facade:
	@classmethod
	def say(cls, what, to):
		print(Speaker.say(what, to))
	def dialog(self, speaker1, speaker2, sentences):
		dialog = Dialog(speaker1, speaker2)
		dialog.sentences = sentences
		print(dialog())

Facade.say('hello', 'World')

facade = Facade()
facade.dialog('Plic', 'Ploc', ['Nice factory', 'It works!'])

