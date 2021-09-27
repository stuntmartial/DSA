class Dir_graph:
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
		self.edges+=1

	def find_indeg(self):
		indeg={v:0 for v in self.d.keys()}
		for i in self.d.keys():
			for j in self.d[i]:
				indeg[j]+=1

		print(indeg)
		return indeg

	def topo_sort(self):
		indeg=self.find_indeg()
		visited_dict={v:0 for v in self.d.keys()}
		q=[]
		count=0
		for i in self.d.keys():
			if indeg[i]==0:
				q.append(i)
				visited_dict[i]=1
		
		oplist=[]

		while len(q)>0:
			print("queue---> ",q)
			v=q.pop(0)
			for i in self.d[v]:
				indeg[i]-=1

			oplist.append(v)
			count+=1

			for i in self.d.keys():
				if indeg[i]==0 and visited_dict[i]==0:
					visited_dict[i]=1
					q.append(i)


		print(oplist)
		if count != len(self.d.keys()):
			print("Graph not a DAG")
			return

		print(oplist)

g = Dir_graph()
'''
while True:

    x = int(input("Enter choice:"))
    if x == 1:
        g.add_node(input("Enter node : "))
    elif x == 2:
        g.add_edge(input("Enter node1 : "),input("Enter node2 : "))
    elif x == 3 :
        g.topo_sort()
    else:
        print("Terminating...")
        break
'''

g.add_edge(5,3)
g.add_edge(5,0)
g.add_edge(3,0)
g.add_edge(3,2)
g.add_edge(2,1)
g.add_edge(4,1)
g.add_edge(4,0)
g.topo_sort()




