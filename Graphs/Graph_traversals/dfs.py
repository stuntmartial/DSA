class Graph:

	def __init__(self):
		self.d = dict()
		self.nodes = 0
		self.edges = 0

	def add_node(self,name):
		self.d[name] = list()
		self.nodes += 1
		print("Node added")

	def add_edge(self,v1,v2):
		if v1 not in self.d.keys():
			self.d[v1] = list()
		if v2 not in self.d.keys():
			self.d[v2] = list()

		self.d[v1].append(v2)
		#self.d[v2].append(v1)

		self.edges += 1
		print("Edge added")

	def dfs(self,starting_node):

		if self.edges == 0:
			print("No edges")
			return 

		ht = dict()
		ht[starting_node] = 1

		for i in self.d.keys():
			if i != starting_node:
				ht[i] = 0

		s = list()
		s.append(starting_node)

		while(len(s)>0):

			v = s.pop(len(s)-1)

			for i in self.d[v]:
				if ht[i] == 0 :
					s.append(i)
					ht[i] = 1

			print(v)

g = Graph()
while True:

    x = int(input("Enter choice:"))
    if x == 1:
        g.add_node(input())
    elif x == 2:
        g.add_edge(input(),input())
    elif x == 3 :
        g.dfs("v1")
    else:
        print("Terminating...")
        break
