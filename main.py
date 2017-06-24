from classes.graph import Graph
from classes.parsers import Parser
from classes.extract import Extract

import classes

if __name__=="__main__":
	question="There are 6 students in the class and 18 candies. If candies are divided equally among students, how many does each student get?"
	a=Extract(question)
	dep=a.dependency_parsing()
	print(a.noun_dependents(dep))
	a.stanford_dep_par()