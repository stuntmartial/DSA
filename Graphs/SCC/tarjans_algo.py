discovery_constant=0
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

	def dfs_helper(self,starting_node,visited_dict,stack,discovery_time,llv):
		global discovery_constant

		print("Current node ---> ",starting_node)
		visited_dict[starting_node]=1
		stack.append(starting_node)
		discovery_constant+=1
		discovery_time[starting_node]=discovery_constant
		llv[starting_node]=discovery_constant

		for i in self.graph[starting_node]:
			if visited_dict[i]==0:
				self.dfs_helper(i,visited_dict,stack,discovery_time,llv)
				llv[starting_node]=min(llv[starting_node],llv[i])
				
			elif visited_dict[i]==1 and (i in stack):
				llv[starting_node]=min(llv[starting_node],llv[i])

		stack.pop(len(stack	)-1)
		print(stack)

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
			l=self.dfs_helper2(i,visited_dict)
			for j in l:
				list_of_nodes.append(j)

		return list_of_nodes

	def trajans_algo(self):
		list_of_nodes=self.dfs()
		print("list_of_nodes-->",list_of_nodes)
		discovery_constant=0
		discovery_time={i:None for i in list_of_nodes}
		llv={i:None for i in list_of_nodes}
		visited_dict={i:0 for i in list_of_nodes}

		for i in list_of_nodes:
			if visited_dict[i]==0:
				self.dfs_helper(i,visited_dict,[],discovery_time,llv)

		scc_dict={}
		for i in llv.keys():
			try:
				scc_dict[llv[i]].append(i)
			except:
				scc_dict[llv[i]]=[i]

		print(scc_dict)
		scc_list=[]
		for i in scc_dict.keys():
			scc_list.append(scc_dict[i])

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
    elif x==3:
    	g.disp()
    elif x==5:
    	g.dfs()
    elif x==6:
    	g.trajans_algo()
    else:
        print("Terminating...")
        break


