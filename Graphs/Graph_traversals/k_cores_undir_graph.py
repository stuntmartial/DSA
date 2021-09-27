class Graph:

	def __init__(self):
		self.d = dict()
		self.nodes = 0
		self.edges = 0

	def add_node(self,name):
		self.d[name] = list()
		self.nodes += 1
		print("Node added")

	def addEdge(self,v1,v2):
		if v1 not in self.d.keys():
			self.add_node(v1)
		if v2 not in self.d.keys():
			self.add_node(v2)

		self.d[v1].append(v2)
		self.d[v2].append(v1)

		self.edges += 1
		print("Edge added")

	def k_cores(self,k):
		included_dict=self.dfs(k)
		print(included_dict)
		self.disp()

	def dfs(self,k):

		visited_dict={v:0 for v in self.d.keys()}
		included_dict={v:1 for v in self.d.keys()}

		for i in self.d.keys():
			self.dfs_helper(i,visited_dict,included_dict,k)

		self.disp()

		return included_dict

	def dfs_helper(self,starting_node,visited_dict,included_dict,k):
		print("Visiting ",starting_node)
		visited_dict[starting_node]=1
		if len(self.d[starting_node])<k:
			self.remove_connections(starting_node)
			included_dict[starting_node]=0
			return

		for i in self.d[starting_node]:
			if visited_dict[i]==0:
				self.dfs_helper(i,visited_dict,included_dict,k)

		if len(self.d[starting_node])<k:
			self.remove_connections(starting_node)

	def remove_connections(self,node):
		print("remove_connections working on ",node)
		print(node," --> ",self.d[node])
		for i in self.d[node]:
			print('i ',i)
			for j in range(len(self.d[i])):
				print(self.d[i][j])
				if self.d[i][j]==node:
					print("Removing",self.d[i][j])
					self.d[i].pop(j)

					break

		self.d[node]=[]
		self.disp()

	def disp(self):
		if self.nodes==0:
			print("No nodes")
			return

		print(self.d)

k = 3; 
g1 = Graph (); 
g1.addEdge(0, 1) 
g1.addEdge(0, 2) 
g1.addEdge(1, 2) 
g1.addEdge(1, 5) 
g1.addEdge(2, 3) 
g1.addEdge(2, 4) 
g1.addEdge(2, 5) 
g1.addEdge(2, 6) 
g1.addEdge(3, 4) 
g1.addEdge(3, 6) 
g1.addEdge(3, 7) 
g1.addEdge(4, 6) 
g1.addEdge(4, 7) 
g1.addEdge(5, 6) 
g1.addEdge(5, 8) 
g1.addEdge(6, 7) 
g1.addEdge(6, 8) 
g1.k_cores(k)
'''
while True:

    x = int(input("Enter choice:"))
    if x == 1:
        g.add_node(input())
    elif x == 2:
        g.add_edge(input(),input())
    elif x == 3:
        g.k_cores(int(input("Enter k :")))
    else:
        print("Terminating...")
        break
'''