""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""

from classes import *

class Graph(object):
    def __init__(self):
        G=nx.DiGraph()
        self.G=G

    def add_nod(self,name):
        self.G.add_node(name)

    def display_graph(self):
        print(nx.degree(self.G))
        print(self.G.nodes(data=True))

    def add_edge(self,node1,node2):
    	self.G.add_edge(node1,node2)

    def add_att(self,node,attr_name,attr_type):
    	self.G.node(node, attr_name=attr_type)

    def add_node_attr(self,node,attr_name,attr_type):
    	if(attr_name=="Head"):
    		self.G.add_node(node, Head=attr_type)

    def att_edge(self,head,node,att_name,att_value):
    	if(att_name=="Relation"):
    		self.G.add_edge(head, node, Relation=att_value )

    def return_node_head(self,node_name):
    	return self.G.node[node_name]["Head"]

    def draw(self):
    	pos=nx.spring_layout(self.G)
    	nx.draw_networkx(self.G,with_labels=True)
    	plt.draw()
    	plt.show()
    	