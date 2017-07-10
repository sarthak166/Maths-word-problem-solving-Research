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
    	print(self.G.node[node1]['name'],self.G.node[node2]['name'])
    	self.G.add_edge(node1,node2)

    def add_att(self,node,attr_name,attr_type):
    	self.G.node(node, attr_name=attr_type)

    def add_node_attr(self,node,attr_name,attr_type):
    	if(attr_name=="name"):
    		self.G.add_node(node, name=attr_type)

    def att_edge(self,head,node,att_name,att_value):
    	if(att_name=="Relation"):
    		self.G.	add_edge(head, node, Relation=att_value )

    def return_node_head(self,node_name):
    	return self.G.node[node_name]["Head"]

    def draw(self):
    	pos=nx.spring_layout(self.G)
    	nx.draw_networkx(self.G,with_labels=True)
    	plt.draw()
    	plt.show()
    	
    def draw_node_name(self,number):
    	pos = nx.spring_layout(self.G)
    	#nx.draw_networkx(self.G,with_labels=True)
    	#for n,d in self.G.nodes_iter(data=True):
    	#	print(n,d)
    	#for node, position in pos.items():
    	#	print("Printing pos "+str(node),str(position))
    	#	for n,d in self.G.nodes_iter(data=True):
    	#		if node == n:
    	#			x,y=pos[node]
    	#			print(x,y,d)
    	#			plt.text(x,y,d, bbox=dict(facecolor='red', alpha=0.1),horizontalalignment='center')
    		
        	

    	#print(pos['node'])
    	#nx.draw_networkx(self.G,with_labels=True)
    	#for n,d in self.G.nodes_iter(data=True):
    	#	print(n,d)
    	#	x,y=pos[n]
    	#	print(x,y)
    	#	plt.text(x,y,d, bbox=dict(facecolor='red', alpha=0.1),horizontalalignment='center')
    		 	

    	#for i in range(pos):
    	#	for n,d in self.G.nodes_iter(data=True):
    	#		if (n==i):







    	#name=nx.get_node_attributes(self.G,'name')
    	#for i in self.G.nodes_iter(data=True):
    	#	x,y=pos[i]
    	#	if i in name:    			
    	#		print("Printing name"+str(name[i]))
    	#		s=name[i]
    	#		plt.text(x,y,s, bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center') 	
    	#	else:
    	#		pass
    	#no=self.G.nodes()
    	#color=nx.get_node_attributes(self.G,'name')
    	#for i in range(len(no)):
    	#	x,y=self.G.node["name"][i]
    	#	plt.text(x,y+0.1,s='Node word', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center') 
    	nx.draw_networkx(self.G, pos)
    	node_labels=nx.get_node_attributes(self.G,'name')
    	print(node_labels)
    	nx.draw_networkx_labels(self.G, pos, labels = node_labels)
    	#nx.draw_networkx_nodes(self.G,pos,node_labels)
    	# kurs = "%i.png" % number
    	# plt.savefig(kurs, format='png')
    	plt.show()
