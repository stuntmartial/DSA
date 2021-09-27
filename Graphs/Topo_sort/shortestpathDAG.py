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

	def find_longest_path(self):
		l=self.topo_sort()
		INF=999999999
		dist={v:INF for v in self.d.keys()}

		for i in l:
			for j in self.d[i]:
				key=self.get_key(i,j)
				print("key--->",key)
				if dist[i]==INF:
					dist[i]=0
				
				if dist[j]>dist[i]+self.weights[key]:
					dist[j]=dist[i]+self.weights[key]
				
				print(dist)

		for i in dist:
			if dist[i]==0:
				dist[i]=INF

		print(dist)
		op=min([dist[i] for i in dist.keys()])
		print(op)

g=Graph()

g.add_edge(1,2,3)
g.add_edge(3,2,4)
g.add_edge(2,6,2)
g.add_edge(6,4,6)
g.add_edge(6,5,5)
	
g.find_longest_path()