class Dir_graph:

	def __init__(self):
		self.graph = dict()
		self.nodes = 0
		self.edges = 0

	def add_node(self,node):

		if node in self.graph.keys():
			print("Node already present...")
			return

		else:
			self.graph[node] = list()
			self.nodes += 1

	def add_edge(self,node1,node2):

		if node1 not in self.graph.keys():
			self.add_node(node1)
		if node2 not in self.graph.keys():
			self.add_node(node2)

		if node2 in self.graph[node1]:
			return

		self.graph[node1].append(node2)
		self.edges += 1

	def transpose(self):
		if self.nodes==0:
			return None

		transpose_graph=Dir_graph()

		for i in self.graph.keys():
			for j in self.graph[i]:
				transpose_graph.add_edge(j,i)

		transpose_graph.disp()
		return transpose_graph

	def dfs_helper(self,starting_node,visited_dict,l):
		visited_dict[starting_node]=1
		for i in self.graph[starting_node]:
			if visited_dict[i]==0:
				self.dfs_helper(i,visited_dict,l)

		l.append(starting_node)
		print(l)

	def dfs_helper2(self,starting_node,visited_dict):
		visited_dict[starting_node]=1
		s=[starting_node]
		l=list()
		while len(s)>0:
			v=s.pop(len(s)-1)
			for i in self.graph[v]:
				if visited_dict[i]==0:
					visited_dict[i]=1
					s.append(i)

			l.append(v)
		print(l)
		return l

	def dfs(self):
		if self.nodes==0:
			print("No nodes")
			return 

		visited_dict={i:0 for i in self.graph.keys()}
		list_of_nodes=[]
		for i in self.graph.keys():
			if visited_dict[i]!=0:
				continue

			l=[]
			self.dfs_helper(i,visited_dict,l)
			for j in l:
				list_of_nodes.append(j)

		return list_of_nodes

	def kosaraju_algo(self):
		scc_list=[]
		l=self.dfs()
		print(l)
		visited_dict={i:0 for i in self.graph.keys()}
		gt=self.transpose()
		for i in range(len(l)-1,-1,-1):
			if visited_dict[l[i]]!=0:
				continue
			scc=[]
			print("Before ",visited_dict)
			print("starting_node--->",l[i])
			scc=gt.dfs_helper2(l[i],visited_dict)
			print("After ",visited_dict)
			scc_list.append(scc)

		print(scc_list)		

	def disp(self):
		if self.nodes==0:
			print("No nodes")
			return

		for i in self.graph.keys():
			print(i," -> ",self.graph[i])

g = Dir_graph()
while True:

    x = int(input("Enter choice:"))
    if x == 1:
        g.add_node(int(input()))
    elif x == 2:
        g.add_edge(int(input()),int(input()))
    elif x == 3 :
        g.transpose()
    elif x==4:
    	g.disp()
    elif x==5:
    	g.dfs()
    elif x==6:
    	g.kosaraju_algo()
    else:
        print("Terminating...")
        break
