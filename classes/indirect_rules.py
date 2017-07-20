'''Class for defining the rules for indirect dependencies
'''
	
from classes import *

class Indirect_rules(parsers.Parser,graph.Graph):
	'''indirect dependencies from question
	'''

	def __init__(self,dep_parse,question):
		self.dep_parse=dep_parse
		super(Indirect_rules, self).__init__(question)

	