'''
Class to extract information for the question
'''
from classes import *

class Extract(parsers.Parser):

	def __init__(self,question):
		self.question=question

	def noun_dependents(self,dep_parse):
		'''a word's dependencies
		Frist loop is for printing everything
		Second one is for extracting a word head and children dependencies
		
		Arguments:
			dep_parse {[object]} -- [spacy parse]
		
		Returns:
			[list] -- [all noun dependencies]
		'''
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

	def node_pos(self,dep_parse):
		'''Returns list of nodes 
		
		returns noun(container), verb(function) and number(quantity) as nodes after lammatization of a word and removal of 
		stop words
		
		Arguments:
			dep_parse {[parser by spacy parser]} -- [parse of the question]
		
		Returns:
			[list] -- [final node list]
		'''
		dep=[]
		lemmatizer = WordNetLemmatizer()
		stop = set(stopwords.words('english'))
		for word in dep_parse:
			if word.pos_=="NUM" or word.pos_=="NOUN" or word.pos_=="PROPN"or word.pos_=="VERB":
				if word.pos_!="NUM" and word.text not in stop:
					w=lemmatizer.lemmatize(word.text)
					dep.append(w)
				elif word.pos_=="NUM":
					dep.append(word.text)
		return dep

	def question_process(self,dep_parse,node_list):
		'''
		Exatract quantity asked in the question
		
		[description]
		
		Arguments:
			dep_parse {[type]} -- [description]
		'''
		for word in dep_parse:
			if (word.tag_=="WDT" or word.tag_=="WP" or word.tag_=="WP$" or word.tag_=="WRB" or
				word.text=="Find" or word.text=="Calculate" ):
					for word in dep_parse:
						if (word.text in node_list):
							return word.text