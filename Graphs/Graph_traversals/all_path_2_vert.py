l=[]
class Graph:

	def __init__(self):
		self.d = dict()
		self.nodes = 0
		self.edges = 0

	def add_node(self,name):
		self.d[name] = list()
		self.nodes += 1
		print("Node added")

	def add_edge(self,v1,v2):
		if v1 not in self.d.keys():
			self.add_node(v1)
		if v2 not in self.d.keys():
			self.add_node(v2)

		self.d[v1].append(v2)
		#self.d[v2].append(v1)

		self.edges += 1
		print("Edge added")

	def all_path(self,source,destination):
		global l
		l=[]
		visited_dict={i:0 for i in self.d.keys()}
		self.dfs_helper(source,destination,visited_dict,[source])
		print(l)

	def dfs_helper(self,source,destination,visited_dict,curr_path):
		global l
		visited_dict[source]=1
		if source==destination:
			print(curr_path)
			l2=[i for i in curr_path]
			l.append(l2)
		else:
			for i in self.d[source]:
				if visited_dict[i]==0:
					curr_path.append(i)
					self.dfs_helper(i,destination,visited_dict,curr_path)
					curr_path.pop(len(curr_path)-1)

		visited_dict[source]=0

	def disp(self):
		if self.nodes==0:
			print("No nodes")
			return

		print(self.d)


g = Graph()
while True:

    x = int(input("Enter choice:"))
    if x == 1:
        g.add_node(int(input()))
    elif x == 2:
        g.add_edge(int(input()),int(input()))
    elif x==3:
    	g.disp()
    elif x==4:
    	source=int(input("Enter source: "))
    	destination=int(input("Enter destination: "))
    	g.all_path(source,destination)



