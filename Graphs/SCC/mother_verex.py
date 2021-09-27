finishing_time=1
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

	def dfs_helper(self,starting_vertex,visited_dict):
		global finishing_time
		visited_dict[starting_vertex][0]=1
		l=[]
		for i in self.graph[starting_vertex]:
			if visited_dict[i][0]==0:
				self.dfs_helper(i,visited_dict)
				l.append(i)

		visited_dict[starting_vertex][1]=finishing_time
		finishing_time+=1
		print(l)

	def dfs(self):
		global finishing_time
		visited_dict={v:[0,None] for v in self.graph}

		for i in self.graph:
			if visited_dict[i][0]==0:
				self.dfs_helper(i,visited_dict)

		finishing_time=1
		print(visited_dict)
		return visited_dict

	def find_max(self,visited_dict):
		max_finishing_node=list(visited_dict.keys())[0]
		for i in visited_dict.keys():
			if visited_dict[i][1]>visited_dict[max_finishing_node][1]:
				max_finishing_node=i

		return max_finishing_node

	def find_mother_vertex(self):
		visited_dict=self.dfs()
		max_finishing_node=self.find_max(visited_dict)
		visited_dict2={v:[0,None] for v in self.graph}
		self.dfs_helper(max_finishing_node,visited_dict2)
		for i in visited_dict2.keys():
			if visited_dict2[i][0]==0:
				return -1

		return max_finishing_node

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
    elif x==4:
    	g.dfs()
    elif x==5:
    	op=g.find_mother_vertex()
    	print(op)
    else:
        print("Terminating...")
        break

