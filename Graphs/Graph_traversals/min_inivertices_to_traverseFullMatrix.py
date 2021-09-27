class Graph:
	def __init__(self):
		self.d={}
		self.nodes=0
		self.edges=0

	def add_node(self,node):
		if node not in self.d.keys():
			self.d[node]=[]
			self.nodes+=1

	def add_edge(self,node1,node2):
		if node1 not in self.d.keys():
			self.add_node(node1)
		if node2 not in self.d.keys():
			self.add_node(node2)

		if node2 not in self.d[node1]:
			self.d[node1].append(node2)
		if node1 not in self.d[node2]:
			self.d[node2].append(node1)

	def func(self,matrix):
		g=self.convert_to_graph(matrix)
		res=g.dfs()
		print(res)
		return res

	def convert_to_graph(self,matrix):
		g=Graph()
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				si=str(i)
				sj=str(j)
				node=si+','+sj	
				g.add_node(node)

		print(len(matrix))
		print(len(matrix[0]))

		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
					si=str(i)
					sj=str(j)
					si1=str(i+1)
					sj1=str(j+1)
					node=si+','+sj
					node1=si1+','+sj
					node2=si+','+sj1
					
					if i==len(matrix)-1:
						if j==len(matrix[0])-1:
							break
						else:
							g.add_edge(node,node2)
							continue

					if j==len(matrix[0])-1:
						if i==len(matrix)-1:
							break
						else:
							g.add_edge(node,node1)
							continue

					g.add_edge(node,node1)
					g.add_edge(node,node2)

		g.disp()
		return g

	def dfs(self):
		visited_dict={v:0 for v in self.d.keys()}
		list_of_nodes=[]
		for i in list(self.d.keys()):
			list_of_nodes.append(i)
		list_of_starting_nodes=[]

		while True:
			starting_node=self.get_starting_node(matrix,list_of_nodes,visited_dict)
			print("Starting_pos-----> ",starting_node)
			if starting_node==None:
				break
			self.dfs_helper(starting_node,visited_dict,matrix)
			print(visited_dict)
			list_of_starting_nodes.append(starting_node)
			
		print(list_of_starting_nodes)
		return list_of_starting_nodes

	def dfs_helper(self,starting_node,visited_dict,matrix):
		visited_dict[starting_node]=1
		print("visiting--->",starting_node)
		for i in self.d[starting_node]:
			val_start=matrix[int(starting_node[0])][int(starting_node[2])]
			val=matrix[int(i[0])][int(i[2])]
			if visited_dict[i]==0 and val<=val_start:
				self.dfs_helper(i,visited_dict,matrix)

	def get_starting_node(self,matrix,list_of_nodes,visited_dict):
		l=[]
		for i in list_of_nodes:
			if visited_dict[i]==0:
				l.append(i)

		if len(l)==0:
			return None

		max_ele=matrix[int(l[0][0])][int(l[0][2])]
		max_x=int(l[0][0]);max_y=int(l[0][2])

		for i in range(1,len(l)):
			ele = matrix[int(l[i][0])][int(l[i][2])]
			if ele>max_ele:
				max_ele=ele
				max_x=int(l[i][0])
				max_y=int(l[i][2])

		x=str(max_x)
		y=str(max_y)
		starting_node=x+','+y
		return starting_node

	def disp(self):
		if self.nodes==0:
			print("No nodes")
		else:
			print(self.d)

n=int(input("Enter n : "))
print("Enter matrix : ")
matrix=[]
for i in range(n):
	l=[int(i) for i in input().split()]
	matrix.append(l)

for i in range(n):
	for j in range(n):
		print(matrix[i][j],end="")
	print()

g2=Graph()
res=g2.func(matrix)
print(res)