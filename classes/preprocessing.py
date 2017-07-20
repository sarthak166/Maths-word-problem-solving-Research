'''Pre processing of the question

'''
from classes import *

class Preprocessing(parsers.Parser):
	def __init__(self,question):
		self.question=question
		self.word_dic={}
		self.num_dic={}
		super(Preprocessing, self).__init__(question)
		self.question=question
		self.node_list=[]
		self.quantity=0
		self.word_dic={}
		self.li=[]
		self.numeric_li=[]


	def distingush_word(self):
		'''Find the Numeric quantity in the question and iterate over its children and ancestor
		
		Returns:
			[type] -- [description]
		'''
		ques=self.question
		for word in self.parse:
			if(word.dep_=="nummod"):
				qword=word.head.text
				cword=lemmatizer.lemmatize(word.head.text)
				try:
					match = next(val for key, val in self.word_dic.items() if cword in key)
					self.word_dic[cword]=self.word_dic[cword]+1
					#print(self.word_dic[cword])
				except StopIteration:
					self.word_dic[cword]=1
				fword=cword+str(self.word_dic[cword])
				print(fword)
				qword=qword+' '
				fword=fword+' '
				new_question=str.replace(self.question,qword,fword, 1)
				print(new_question)
				self.question=new_question
		self.parse=super(Extract_direct,self).dependency_parsing(self.question)
		print(self.question)
		return self.question

	def node(self):
		'''Adds nodes and specifies its head
		'''
		for word in self.parse:
			#print(word.text,word.head.text,word.dep_,word.pos_)
			if word.pos_=="NUM" or word.pos_=="NOUN" or word.pos_=="PROPN"or word.pos_=="VERB":
				if word.dep_=="nummod":
					#self.quantity=self.quantity+1
					cword=word.head.text
					#cword=lemmatizer.lemmatize(word.head.text)
					#if cword not in self.node_list:
					#	self.node_list.append(cword)
					#cword1=cword+str(self.quantity)
					self.add_numeric(word.text,cword)
				elif word.text not in stop and word.text not in self.node_list:	
					w=lemmatizer.lemmatize(word.text)
					self.node_attr(w,word.pos_)

	def node_attr(self,word,word_pos):
		'''add head attribute of the node
		
		Arguments:
			word {[the name of the node]} 
			word_pos {[poas tag of the word]}
		'''
		if word_pos=="VERB":	
			super(Extract_direct,self).add_node_attr(word,"Head","Function")
			self.node_list.append(word)
		elif word_pos=="NOUN" or word_pos=="PROPN":
			self.node_list.append(word)
			super(Extract_direct,self).add_node_attr(word,"Head","Entity")

	def add_numeric(self,number,container):
		'''Function that makes nodes and defined their head
		
		Takes nodes (only nummod relations and adds their properties) 
		
		Arguments:
			number {[numeric dependent quantity]}
			container {[head of nummod relation]}
		'''
		print("added")
		self.node_list.append(container)
		super(Extract_direct,self).add_node_attr(number,"Head","Quantity")
		super(Extract_direct,self).add_node_attr(container,"Head","Container")
		super(Extract_direct,self).att_edge(container,number,"Relation","Quantity")


	def add_edges(self):
		'''Adds edges between adges
		searches in list of nodes and if there is a dependency add a node
		
		Arguments:
			list_nodes {[list]} -- [list of nodes]
			dep {[object]} -- [spacy parser result]
		'''
		lemmatizer = WordNetLemmatizer()
		for word in self.parse:
			a=lemmatizer.lemmatize(word.text)
			b=lemmatizer.lemmatize(word.head.text)
			if (a in self.node_list and b in self.node_list):
				self.add_egde_attr(a,b,word.dep_)
				#if(self.check_connectivity(a,b)):
					#print(word.text,word.head.text)
		
	def add_egde_attr(self,word,head,dep):
		#if(dep=="nummod"):
		#	print("Adding edge between container and quantity")
		#	super(Extract_direct,self).att_edge(head,word,"Relation","Quantity")	
		#print("Adding edge between container and property")
		super(Extract_direct,self).att_edge(head,word,"Relation","Property")

	def check_connectivity(self,node1,node2):
		if(super(Extract_direct,self).return_node_head(node1)=="Container" and super(Extract_direct,self).return_node_head(node2)["Head"]=="Container"):
			return False
		else:
			return True

	def name_nodes(self,node_list,dep_parse):
		for word in dep_parse:
			if(word.dep_=="nummod"):
				#print(word.text,word.head.text)
				super(Extract_direct,self).add_att()
	
	def sen_tok(self):
		sent_tokenize_list = sent_tokenize(self.question)
		return sent_tokenize_list

	def chunck_question(self):
		'''Takes out question part from the whole question
		'''
		list_q=self.sen_tok()
		question_word=["How","When","What","Find","Calculate"]
		for i in range(len(list_q)):
			for j in range(len(question_word)):
				print(list_q[i],question_word[j])
				if question_word[j] in list_q[i]:
					del list_q[i]
					break
		final_q=' '.join(list_q)
		return final_q