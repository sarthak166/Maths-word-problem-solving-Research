from classes.graph import Graph
from classes.parsers import Parser
from classes.extract import Extract
from classes.make_graph import Make_graph

import classes
'''
imports for function final_list
'''

def final_list(initlist):
	'''
	Function for cleaning list of pos taged words received
	
	Arguments:
		list: with stop words and not lammented
	
	Returns:
		[list] -- [list wothout stop words and lammented words]
	'''
	str1 = ''.join(initlist)
	pas=Parser(str1)
	pastag=pas.pos_tag()
	lemmatizer = WordNetLemmatizer()
	final=[]
	stop = set(stopwords.words('english'))
	print(initlist)
	for i in range(len(initlist)):
		if initlist[i] not in stop and pastag_!="NUM":
			p=lemmatizer.lemmatize(initlist[i])
			final.append(p)
		elif pastag_=="NUM":
			final.append(initlist[i])
	return final

if __name__=="__main__":
	question1="There are 6 students in the class and 18 candies. If candies are divided equally among students, how many does each student get?"
	question="There are 43 rulers in the drawrer. Benny took 27 rulers from the drawrer. How many rulers are now in the drawrer?"
	a=Extract(question)
	dep=a.dependency_parsing()
	a.pos_tag()
	#print(a.noun_dependents(dep))
	#a.stanford_dep_par()
	poslist=a.node_pos(dep)
	g=Make_graph()
	g.add_nodes(poslist)
	g.add_edges(poslist,dep)
	word=a.question_process(dep,poslist)
	g.add_nod("question")
	print(word)
	g.display_graph()
	g.add_edge("question",word)
	g.display_graph()