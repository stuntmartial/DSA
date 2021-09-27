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

	def disp(self):
		if self.nodes==0:
			print("No nodes")
			return

		print(self.d)

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


def find_dict(list_of_words):
	g=Graph()
	for i in range(0,len(list_of_words)-1):
		for j in range(i+1,len(list_of_words)):
			fp=0;sp=0
			while True:
				if list_of_words[i][fp]!=list_of_words[j][sp]:
					g.add_edge(list_of_words[i][fp],list_of_words[j][sp])
					break

				fp+=1
				sp+=1
				if fp==len(list_of_words[i]) or sp==len(list_of_words[j]):
					break

	g.disp()
	g.topo_sort()

list_of_words=["baa", "abcd", "abca", "cab", "cad"]
find_dict(list_of_words)
list_of_words2=["caa", "aaa", "aab"]
find_dict(list_of_words2)