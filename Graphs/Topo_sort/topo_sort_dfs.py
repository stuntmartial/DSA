class Dir_graph:

	def __init__(self):

		self.graph = dict()
		self.nodes = 0
		self.edges = 0
		self.visited_dict = dict()
		self.topo_stk = list()

	def add_node(self,node):

		if node not in self.graph.keys():
			self.graph[node] = list()
			self.nodes += 1
			print("Node added...")

		else:
			print("Node already present")
			return

	def add_edge(self,node1,node2):

		if node1 not in self.graph.keys():
			self.add_node(node1)
		if node2 not in self.graph.keys():
			self.add_node(node2)

		self.graph[node1].append(node2)
		self.edges += 1
		print("Edge added")

	def toposort_helper(self,node):

		self.visited_dict[node] = 1

		for i in self.graph[node]:
			if self.visited_dict[i] == 0:
				self.toposort_helper(i)

		self.topo_stk.append(node)
		
	def toposort(self):

		
		for i in self.graph.keys():
			self.visited_dict[i] = 0

		for i in self.graph.keys():

			if self.visited_dict[i] == 0:
				self.toposort_helper(i)

		for i in range(len(self.topo_stk)-1,-1,-1):
			print(self.topo_stk[i] , end = "\t")
		print()

g = Dir_graph()
'''
while True:

    x = int(input("Enter choice:"))
    if x == 1:
        g.add_node(input())
    elif x == 2:
        g.add_edge(input(),input())
    elif x == 3 :
        g.toposort()
    else:
        print("Terminating...")
        break
'''
g.add_edge(5,3)
g.add_edge(5,0)
g.add_edge(3,0)
g.add_edge(3,2)
g.add_edge(2,1)
g.add_edge(4,1)
g.add_edge(4,0)
g.toposort()
