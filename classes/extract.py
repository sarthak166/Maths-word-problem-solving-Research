'''
Class to extract information for the question
'''
from classes import *

class Extract(parsers.Parser):

	def __init__(self,question):
		self.question=question

	def noun_dependents(self,dep_parse):
		noun_dep=[]
		for word in dep_parse:
			if word.pos_=="NUM" or word.pos_=="NOUN" or word.pos_=="PROPN"or word.pos_=="VERB":
				print(word.text, word.pos_, word.dep_, word.head.text)
		print("printing noun")
		for possible_noun in dep_parse:
			for i in possible_noun.children:	
				if i.pos_=="NOUN" or i.pos_=="NUM":
					print(i,possible_noun,possible_noun.dep_)
			if possible_noun.pos_ == "NOUN":
				for i in possible_noun.children:
					print(i,possible_noun,possible_noun.dep_)
		return noun_dep
