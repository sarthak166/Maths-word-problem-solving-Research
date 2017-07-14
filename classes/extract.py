'''
Class to extract direct information for the question
'''
from classes import *

class Extract_direct(graph.Graph,parsers.Parser):

	def __init__(self,question,parse):
		self.question=question
		self.parse=parse
		self.node_list=[]
		super(Extract_direct, self).__init__()
		self.quantity=0
		self.word_dic={}
		self.li=[]
		self.numeric_li=[]

	
	def sen_tok(self):
		sent_tokenize_list = sent_tokenize(self.question)
		return sent_tokenize_list

	def numeric_dep(self):
		for word in self.parse:
			print(word.head.text,word.text,word.dep_)
		for word in self.parse:
			#print(word.head.text,word.text,word.dep_)
			if(word.pos_=="NUM"):
				self.li.append(self.position(word))
				#print("Printing numeric relations")
				self.add_name_node(word)
				for child in word.children:
					if self.check_pos(child) and self.remove_stopwords(child):
						self.add_name_node(child)
						super(Extract_direct,self).add_edge(self.position(str(word.text)),self.position(str(child)))	
						self.li.append(self.position(child))
						self.recurse(child,word)
					else:
						self.li.append(self.position(child))
						self.recurse(child,word)
				for ans in word.ancestors:
					if self.check_pos(ans) and self.remove_stopwords(ans):
						self.add_name_node(ans)
						super(Extract_direct,self).add_edge(self.position(str(word.text)),self.position(str(ans)))	
						self.li.append(self.position(ans))
						self.recurse(ans,word)
					else:
						self.li.append(self.position(ans))
						self.recurse(ans,word)
	
	def recurse(self,ite_word,prev_word):
		#print("main word"+str(ite_word))
		#print("Printing nodes"+str(self.numeric_li))
		print("Printig in recurse"+str(ite_word.text),str(prev_word))	
		for word in self.parse:
			if (str(word.text) == str(ite_word)):
				for child in word.children:
					#print("Children is "+ str(child),str(self.li))
					if self.position(child) not in self.li and self.check_pos(child) :
						self.add_name_node(child)
						if self.check_pos(word) :
							self.add_name_node(word)
							prev_word=child
							super(Extract_direct,self).add_edge(self.position(str(word.text)),self.position(str(child)))	
							#self.li.append(self.position(child))				
							self.recurse(child,prev_word)
					elif self.position(child) not in self.li and self.check_pos(word) :
						print("in ahlf half"+str(prev_word.text),str(word.text))
						super(Extract_direct,self).add_edge(self.position(str(word.text)),self.position(prev_word))
						prev_word=word
						#self.li.append(self.position(child))				
						self.recurse(child,prev_word)
					elif self.position(child) not in self.li:
						#self.li.append(self.position(child))
						self.recurse(child,prev_word)
				for ans in word.ancestors:
					#print("Anscester is "+str(ans),str(self.li))
					if self.position(ans) not in self.li and self.check_pos(ans) :
						#print("goes into"+str(ans))
						self.add_name_node(ans)
						if self.check_pos(word) :
							self.add_name_node(word)
							prev_word=ans
							super(Extract_direct,self).add_edge(self.position(str(word.text)),self.position(str(ans)))	
							self.li.append(self.position(ans))
							self.recurse(ans,prev_word)
					elif self.position(ans) not in self.li and self.check_pos(word):
						print("in ans half"+str(prev_word.text),str(word.text))
						super(Extract_direct,self).add_edge(self.position(str(word.text)),self.position(prev_word))
						prev_word=word
						self.li.append(self.position(ans))				
						self.recurse(ans,prev_word)
					elif self.position(ans) not in self.li:
						self.li.append(self.position(ans))				
						self.recurse(ans,prev_word)


	def position(self,child):
		y=self.question.find(str(child))
		#print(str(child) +' '+str(y))
		return y

	def add_name_node(self,child):
		a=self.position(child)
		self.numeric_li.append(child)
		super(Extract_direct,self).add_node_attr(a,"name",child)

	def check_pos(self,ans):
		if (ans.pos_=="NOUN" or ans.pos_=="PROPN" or ans.pos_=="VERB" or ans.pos_=="NUM" or ans.pos_=="ADJ"):
			return True
		else:
			return False

	def remove_stopwords(self,word):
		if word.text.lower() not in stop:
			return True
		else:
			return False