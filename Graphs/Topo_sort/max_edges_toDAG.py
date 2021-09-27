class Graph:
	def __init__(self):
		self.d={}
		self.nodes=0
		self.edges=0

	def add_node(self,node):
		if node not in self.d.keys():
			self.d[node]=[]
			self.nodes+=1
			print("Node added....")

	def add_edge(self,node1,node2):
		if node1 not in self.d.keys():
			self.add_node(node1)
		if node2 not in self.d.keys():
			self.add_node(node2)

		self.d[node1].append(node2)
		self.edges+=1
		print("Edge added")

	def topo_sort_helper(self,node,visited_dict,rec_stk):
		if visited_dict[node]==1:
			return

		visited_dict[node]=1

		for i in self.d[node]:
			if visited_dict[i]==0:
				self.topo_sort_helper(i,visited_dict,rec_stk)

		rec_stk.append(node)

	def topo_sort(self):
		visited_dict={v:0 for v in self.d.keys()}
		rec_stk=[]

		for i in self.d.keys():
			if visited_dict[i]==0:
				self.topo_sort_helper(i,visited_dict,rec_stk)

		op=[rec_stk[i] for i in range(len(rec_stk)-1,-1,-1)]
		print("topo_sort--->",op)
		return op

	def add_max_edges(self):
		l=self.topo_sort()

		for i in range(len(l)-1):
			print("Working on node....",i)
			for j in range(i+1,len(l)):
				if (l[i]!=l[j]) and (l[j] not in self.d[l[i]]) :
					self.add_edge(l[i],l[j])

		for i in self.d.keys():
			print(i,"--->",self.d[i]) 

g=Graph()
g.add_edge(5, 2) 
g.add_edge(5, 0) 
g.add_edge(4, 0) 
g.add_edge(4, 1) 
g.add_edge(2, 3) 
g.add_edge(3, 1)

print(g.d)
g.add_max_edges()