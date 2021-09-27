class Graph:
	def __init__(self):
		self.d={}
		self.weights={}
		self.nodes=0
		self.edges=0

	def add_node(self,node):
		if node not in self.d.keys():
			self.d[node]=[]
			self.nodes+=1
			print("Node added....")

	def get_key(self,node1,node2):
		key=str(node1)+str(node2)
		return key

	def add_edge(self,node1,node2,weight):
		if node1 not in self.d.keys():
			self.add_node(node1)
		if node2 not in self.d.keys():
			self.add_node(node2)

		self.d[node1].append(node2)
		key=self.get_key(node1,node2)
		self.weights[key]=weight
		self.edges+=1
		print("Edge added")

	
	
	def find_longest_path(self):
		l=self.topo_sort()
		NINF=-999999999
		dist={v:0 for v in self.d.keys()}

		for i in l:
			for j in self.d[i]:
				key=self.get_key(i,j)
				if dist[j]<dist[i]+self.weights[key]:
					dist[j]=dist[i]+self.weights[key]

		print(dist)

g=Graph()

g.add_edge(1,2,3)
g.add_edge(3,2,4)
g.add_edge(2,6,2)
g.add_edge(6,4,6)
g.add_edge(6,5,5)
	
g.find_longest_path()