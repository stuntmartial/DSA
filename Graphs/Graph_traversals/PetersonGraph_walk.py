class Node:
	def __init__(self,val,alphabet):
		self.alphabet=alphabet
		self.val=val

class Graph:
	def __init__(self):
		self.d={}
		self.nodes=0
		self.edges=0

	def add_node(self,node):
		if node not in self.d.keys():
			self.d[node]=[]
			#print(node.val,node.alaphabet,self.d[node])
			self.nodes+=1

	def add_edge(self,node1,node2):
		#print("node1--->",node1.val,node1.alaphabet)
		if node1 not in self.d.keys():
			self.add_node(node1)
		if node2 not in self.d.keys():
			self.add_node(node2)

		#print(node1.val,node2.val," present")

		if node2 not in self.d[node1]:
			self.d[node1].append(node2)
		if node1 not in self.d[node2]:
			self.d[node2].append(node1)

		self.edges+=1
		#print("Edge added ...")

	def chk_Peterson_path(self,path):
		if path==None:
			print("No path given")
			return

		index=0
		walk=""
		visited_dict={v:0 for v in self.d.keys()}
		ele=path[index]
		starting_node_list=[]
		for i in self.d.keys():
			if ele==i.alphabet:
				starting_node_list.append(i)

		print("starting_node_list---->")
		for i in starting_node_list:
			print(i.val,i.alphabet)

		op1=op2=0
		op1=self.dfs_helper(path,index,visited_dict,walk+str(starting_node_list[0].val),starting_node_list[0],0)
		if op1==0:
			op2=self.dfs_helper(path,index,visited_dict,walk+str(starting_node_list[1].val),starting_node_list[1],0)

		print(op1,op2)
		if op1==op2==0:
			print("path not found...")

	def dfs_helper(self,path,index,visited_dict,walk,starting_node,op):
		if index==len(path)-1:
			print(walk)
			op=1
			return 1

		print("starting_node--->",starting_node.val,starting_node.alphabet,"index--->",index)
		flag=0
		visited_dict[starting_node]=1
		for i in self.d[starting_node]:

			if visited_dict[i]==0 and path[index+1]==i.alphabet:
				visited_dict[i]=1
				#print(starting_node_list[0].val,starting_node_list[0].alaphabet)
				flag=1
				return self.dfs_helper(path,index+1,visited_dict,walk+str(i.val),i,op)

		if flag==0:
			#print("No path found...")
			return op

	def disp(self):
		if self.nodes==0:
			print("No nodes present...")

		for i in self.d:
			print(i.val,i.alaphabet,"--->",end="")
			for j in self.d[i]:
				print(j.val,j.alaphabet," ",end="")
			print()
		print()

g=Graph()
node0=Node(0,'A')
node1=Node(1,'B')
node2=Node(2,'C')
node3=Node(3,'D')
node4=Node(4,'E')
node5=Node(5,'A')
node6=Node(6,'B')
node7=Node(7,'C')
node8=Node(8,'D')
node9=Node(9,'E')

#g.disp()
#print("Adding edges...")
g.add_edge(node0,node1)
g.add_edge(node0,node4)
g.add_edge(node0,node5)
g.add_edge(node1,node2)
g.add_edge(node1,node6)
g.add_edge(node2,node3)
g.add_edge(node2,node7)
g.add_edge(node3,node4)
g.add_edge(node3,node8)
g.add_edge(node4,node9)
g.add_edge(node5,node8)
g.add_edge(node5,node7)
g.add_edge(node9,node6)
g.add_edge(node9,node7)
g.add_edge(node8,node6)
#print("Edges added...")

#g.disp()

path=input("Enter path : ")
g.chk_Peterson_path(path)

