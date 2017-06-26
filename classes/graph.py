""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""

from classes import *

class Graph(object):
    def __init__(self):
        G=nx.Graph()
        self.G=G

    def add_nod(self,name):
        self.G.add_node(name)

    def display_graph(self):
        print(nx.degree(self.G))

    def add_edge(self,node1,node2):
    	self.G.add_edge(node1,node2)