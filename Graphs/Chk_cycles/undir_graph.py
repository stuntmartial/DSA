flag=0
class UnDir_graph:

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

		self.graph[node1].append(node2)
		self.graph[node2].append(node1)
		self.edges += 1

	def chk_cycle(self):
		global flag
		visited_dict={v:0 for v in self.graph.keys()}
		rec_stk=[]
		parent_dict={}

		for i in self.graph.keys():
			if visited_dict[i]==0:
				self.dfs_helper(i,visited_dict,rec_stk,parent_dict)
		
		print(flag)

	def dfs_helper(self,node,visited_dict,rec_stk,parent_dict):
		global flag
		visited_dict[node]=1
		rec_stk.append(node)

		for i in self.graph[node]:
			if visited_dict[i]==0:
				parent_dict[i]=node
				self.dfs_helper(i,visited_dict,rec_stk,parent_dict)
			elif visited_dict[i]==1 and parent_dict[node]!=i:
				if i in rec_stk:
					flag=1
					return
				else:
					continue

		rec_stk.pop(len(rec_stk)-1)

g = UnDir_graph()
while True:

    x = int(input("Enter choice:"))
    if x == 1:
        g.add_node(input())
    elif x == 2:
        g.add_edge(input(),input())
    elif x == 3 :
        g.chk_cycle()
    else:
        print("Terminating...")
        break
