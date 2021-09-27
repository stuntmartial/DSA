class Graph:
	def __init__(self):
		self.d={}
		self.nodes=0
		self.edges=0

	def add_node(self,node):
		if node not in self.d.keys():
			self.d[node]=[]
			self.nodes+=1
			#print("Node added....")

	def add_edge(self,node1,node2):
		if node1 not in self.d.keys():
			self.add_node(node1)
		if node2 not in self.d.keys():
			self.add_node(node2)

		self.d[node1].append(node2)
		self.edges+=1
		#print("Edge added")

	def find_indegree(self):
		indeg={v:0 for v in self.d.keys()}
		for i in self.d.keys():
			for j in self.d[i]:
				indeg[j]+=1

		print(indeg)
		return indeg

	def all_topos(self):
		indeg=self.find_indegree()
		print(self.d.keys())
		visited_dict={v:0 for v in self.d.keys()}
		curr_res=[]
		res=[]
		self.all_topos_helper(indeg,visited_dict,curr_res,res)
		for i in res:
			print(i)

	def all_topos_helper(self,indeg,visited_dict,curr_res,res):
		
		for i in self.d.keys():
			if indeg[i]==0 and visited_dict[i]==0:
				#print("i---->",i)
				for j in self.d[i]:
					indeg[j]-=1

				#print("indeg after deleting ",i,"--->",indeg)

				visited_dict[i]=1
				curr_res.append(i)
				self.all_topos_helper(indeg,visited_dict,curr_res,res)
				curr_res.pop(len(curr_res)-1)


				visited_dict[i]=0
				for j in self.d[i]:
					indeg[j]+=1

				#print("Resetting indeg...",indeg)
		
		#print("curr_res--->",curr_res)
		li=[i for i in curr_res]
		if len(li)==len(list(self.d.keys())):
			res.append(li)

g=Graph()
g.add_edge(5,2)
g.add_edge(5,0) 
g.add_edge(4,0) 
g.add_edge(4,1) 
g.add_edge(2,3) 
g.add_edge(3,1) 

g.all_topos()
