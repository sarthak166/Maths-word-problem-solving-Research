from classes.graph import Graph
from classes.parsers import Parser
from classes.extract import Extract_direct
import pandas as pd
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

def read(name):
	train = pd.read_csv(name, error_bad_lines=False, header=0)
	return train


if __name__=="__main__":
	question1="There are 6 Students in the class and 18 candies. If candies are divided equally among students, how many does each student get?"
	question="There are 43 rulers in the drawrer. Benny took 27 rulers from the drawrer. How many rulers are now in the drawrer?"
	question2="Gwen was organizing her book case making sure each of the shelves had exactly 9 books on it. She has 2 types of books - mystery books and picture books. If she had 3 shelves of mystery books and 5 shelves of picture books,how many books did she have total?"
	li=['Mommy bought 4 egg cartons, and each had 6 eggs.  2 of the eggs were bad. How many good eggs did Mommy get?',
	"Johnson's ordered 4 pizzas, sliced into 4 pieces each. This time the dog ate 1 piece. How many pieces did the people eat?",
	"Joe has 3 friends who all have 5 toy cars, and then 2 friends who only have 2 cars. How many cars do Joe's friends have?",
	"Carol went to the store 4 times last month. She buys 63 eggs each time she goes to the store. How many eggs did Carol buy last month?",
	"Eric starts with 8 cards. He gives 4 to Amanda. How many cards does Eric end with?",
	"Angela removes 80 blocks from a jar. There were originally 83 blocks and 8 pencils in the jar. How many blocks are left in the jar?"
	]

	# for i in range(len(li)):
	# 	final_q=li[i]
	# 	print(final_q)
	# 	parse=Parser(final_q)
	# 	dep=parse.dependency_parsing(final_q)
	# 	parse.pos_tag()
	# 	g=Extract_direct(final_q,dep)
	# 	tok_ques=g.sen_tok()
	# 	g.numeric_dep()
	# 	#g.numeric_dep()
	# 	#g.node()
	# 	#g.add_edges()
		
	# 	g.draw_node_name(i)


	final_q=li[0]
	print(final_q)
	parse=Parser(final_q)
	dep=parse.dependency_parsing(final_q)
	parse.pos_tag()
	g=Extract_direct(final_q,dep)
	tok_ques=g.sen_tok()
	g.numeric_dep()
	#g.numeric_dep()
	#g.node()
	#g.add_edges()
	
	g.draw_node_name(1)