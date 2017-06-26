'''
	Class to do NER taggng, pos tagging, parsing, dependency parsing, coreference resolution using libraries
'''
from classes import *

class Parser():

	def __init__(self,question):
		'''
			Initialising the question
		'''
		self.question=question

	def dependency_parsing(self):
		'''Dependensy parsing using spacy
		
		Returns:
			parsing result
		'''
		doc=nlp(self.question)
		return doc

	def stanford_dep_par(self):
		'''
		Dependency parsing through Stanford parser
		'''
		for i in sent_tokenize(self.question):
			result = dependency_parser.raw_parse(i)
			dep = result.__next__()
			for triple in dep.triples():
				print(triple)

	def pos_tag(self):
		'''
		POS tagging using spacy parser
	
		'''
		doc=nlp(self.question)
		for word in doc:
			print(word.text,word.tag_)