'''Class for defining the rules for indirect dependencies
'''
	
from classes import *

class Indirect_rules(parsers.Parser):
	'''indirect dependencies from question
	'''

	def __init__(self,dep_parse):
		self.dep_parse=dep_parse