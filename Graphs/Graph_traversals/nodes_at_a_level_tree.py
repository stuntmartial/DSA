class Tree:

	def __init__(self):
		self.d = dict()
		self.nodes = 0
		self.edges = 0

	def add_node(self,n):
		self.d[n] = list()
		self.nodes += 1
		print("Node added")

	def add_edge(self,v1,v2):

		if v1 not in self.d.keys():
			self.add_node(v1)
		if v2 not in self.d.keys():
			self.add_node(v2)

		self.d[v1].append(v2)
		self.d[v2].append(v1)

		self.edges += 1
		print("Edge added")

	def nodes_at_a_level(self,root):

		if root not in self.d.keys():
			print("Enter valid root")
			return

		levels = dict()
		visited = dict()
		for i in  self.d.keys():
			visited[i] = 0

		visited[root] = 1

		q = list()
		q.append(root)
		levels[root] = 0

		while(len(q)!=0):

			v = q.pop(0)

			for i in self.d[v]:
				if visited[i] != 1:
					levels[i] = levels[v] + 1
					q.append(i)
					visited[i] = 1

		print(levels)


t = Tree()
while True:

    x = int(input("Enter choice:"))
    if x == 1:
        t.add_node(input())
    elif x == 2:
        t.add_edge(input(),input())
    elif x == 3 :
        t.nodes_at_a_level('0')
    else:
        print("Terminating...")
        break
