class Graph:

	def __init__(self):
		self.d = {}

	def add_node(self,name):
		self.d[name] = list()

	def add_edge(self,v1,v2):
		if v1 not in self.d.keys():
			self.add_node(v1)
		if v2 not in self.d.keys():
			self.add_node(v2)

		self.d[v1].append(v2)
		self.d[v2].append(v1) #for directed graph this should be ommitted

	def print_nodes_edges(self):
		if len(self.d.keys()) == 0 :
			print("No nodes are present")
		if len(self.d.values()) == 0:
			print("No edges are present")
		else:
			print("Nodes ---> ",[i for i in self.d.keys()])
			print("Edges ---> ",[i for i in self.d.values()])

g = Graph()

while True:

	x = int(input())
	if x == 1:
		g.add_node(input())
	elif x == 2:
		g.add_edge(input(),input())
	elif x == 3 :
		g.print_nodes_edges()
	else:
		print("Terminating...")
		break