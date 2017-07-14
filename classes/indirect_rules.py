'''Class for defining the rules for indirect dependencies
'''
	
from classes import *

class Indirect_rules(parsers.Parser):
	'''indirect dependencies from question
	'''

	def __init__(self,dep_parse,question):
		self.dep_parse=dep_parse
		super(Indirect_rules, self).__init__(question)

	def word_quantifier(self):
		print("Here in word quantifiers")
		word_quan=self.read_file()
		#print (s for s in word_quan if self.question in s)
		for i in range(len(word_quan)):
			if word_quan[i] in self.question:
				print(word_quan[i])
		
	def read_file(self):
		print("Reading file")
		quan_list=super(Indirect_rules,self).read('/home/puru/Documents/maths word problem/interlingua/data/word_quan.csv')
		return quan_list["Quantifier"] 
		
