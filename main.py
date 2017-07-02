from classes.graph import Graph
from classes.parsers import Parser
from classes.extract import Extract_direct

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
	question2="Gwen was organizing her book case making sure each of the shelves had exactly 9 books on it. She has 2 types of books - mystery books and picture books. If she had 3 shelves of mystery books and 5 shelves of picture books,how many books did she have total?"
	final_q=question
	parse=Parser(final_q)
	dep=parse.dependency_parsing(final_q)
	parse.pos_tag()
	g=Extract_direct(final_q,dep)
	tok_ques=g.sen_tok()
	g.distingush_numeric()
	g.node()
	g.add_edges()
	g.draw()
	print("running")