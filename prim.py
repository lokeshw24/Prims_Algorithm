#!/bin/python

class Node :
	name=None
	key=None
	neighbours=[]

	def __init__(self, name, neighbours):
		self.name=name
		self.neighbours=neighbours


	def display_neighbours(self):
		print "(",self.name ,")-->"
		for i in self.neighbours : 
			print i;

class Graph :
	All_Nodes=[]
	Edge_Weights={}

	def add_node( self, node, neighbours ):
		n = Node( node, neighbours)
		self.All_Nodes.append(n)

	def print_nodes(self):
		for nodes in self.All_Nodes :
			nodes.display_neighbours()

	def assign_edge_weights(self, node1, node2, edge_weight):
		edge_name=node1+'-'+node2
		self.Edge_Weights[edge_name]=edge_weight

	def get_neighbours(self, node_name) :
		for nodes in self.All_Nodes :
			if( nodes.name==node_name ) :
				neighbours=nodes.neighbours

		return neighbours

	def prim_algo(self, root):
		min_priority_queue={}
		for nodes in self.All_Nodes :
			if( nodes.name==root ) :
				nodes.key=0
			else :
				nodes.key=9999999
			min_priority_queue[nodes.name]=nodes.key

		while min_priority_queue :
			#get the node-name from the queue that has the minimum key-value
			node_with_min_key=min(min_priority_queue, key=min_priority_queue.get)
			del min_priority_queue[node_with_min_key]
			print node_with_min_key

			target_neighbours=self.get_neighbours(node_with_min_key)

			#delete nodes already visited
			for every_neigh in target_neighbours :
				if every_neigh not in min_priority_queue :
					target_neighbours.remove(every_neigh)

			for every_neigh in target_neighbours :
				edge_name=node_with_min_key+'-'+every_neigh
				if ( not( edge_name in self.Edge_Weights ) ):
					edge_name=every_neigh+'-'+node_with_min_key
				
				for nodes in self.All_Nodes :
					if nodes.name==every_neigh and self.Edge_Weights[edge_name]<nodes.key :
						nodes.key=self.Edge_Weights[edge_name]
						min_priority_queue[nodes.name]=nodes.key


def init_graph(my_graph) :
	my_graph.add_node('a', ['b','c'])
	my_graph.add_node('b', ['a','c','d'])
	my_graph.add_node('c', ['a','b','d','e'])
	my_graph.add_node('d', ['b','c'])
	my_graph.add_node('e', ['c'])
	
	my_graph.assign_edge_weights('a', 'b', 2)
	my_graph.assign_edge_weights('a', 'c', 1)
	my_graph.assign_edge_weights('c', 'b', 3)
	my_graph.assign_edge_weights('c', 'd', 12)
	my_graph.assign_edge_weights('c', 'e', 5)
	my_graph.assign_edge_weights('b', 'd', 3)

def main():
	my_graph = Graph()
	init_graph(my_graph)
	my_graph.print_nodes()

	my_graph.prim_algo('c')

main()
