'''
Class to add the semantic information from the text to the 

[description]
'''
from classes import *


class Make_graph(graph.Graph):

	def add_nodes(self,list_nodes):
		for i in range(len(list_nodes)):
			super(Make_graph,self).add_nod(list_nodes[i])
		super(Make_graph,self).display_graph()

	def add_edges(self,list_nodes,dep):
		'''Adds edges between adges
		searches in list of nodes and if there is a dependency add a node
		
		Arguments:
			list_nodes {[list]} -- [list of nodes]
			dep {[object]} -- [spacy parser result]
		'''
		lemmatizer = WordNetLemmatizer()
		for word in dep:
			print(word.text, word.pos_, word.dep_, word.head.text)
		print(list_nodes)
		for word in dep:
			a=lemmatizer.lemmatize(word.text)
			b=lemmatizer.lemmatize(word.head.text)
			if (a in list_nodes and b in list_nodes):
				print(word.text,word.head.text)
				super(Make_graph,self).add_edge(a,b)
		super(Make_graph,self).display_graph()

	def name_nodes(self,node_list,dep_parse):
		for word in dep_parse:
			if(word.dep_=="nummod"):
				print(word.text,word.head.text)