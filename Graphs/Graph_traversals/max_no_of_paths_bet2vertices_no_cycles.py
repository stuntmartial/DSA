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
			self.d[v1] = list()
		if v2 not in self.d.keys():
			self.d[v2] = list()

		self.d[v1].append(v2)


		self.edges += 1
		print("Edge added")

	def max_path(self,starting_node,destination_node):

		global count 

		if starting_node not in self.d.keys() or destination_node not in self.d.keys():
			print("Not in dict")
			return count

		else:
			self.find_max_path(starting_node,destination_node)
			print(count)

	def find_max_path(self,starting_node,destination_node):

		global count
		if starting_node == destination_node:
			count+=1

		else:

			for i in self.d[starting_node]:
				self.find_max_path(i,destination_node)
				
		


count = 0
g = Graph()
while True:

    x = int(input("Enter choice:"))
    if x == 1:
        g.add_node(input())
    elif x == 2:
        g.add_edge(input(),input())
    elif x == 3 :
        count = 0
        g.max_path(input("Enter source vertex: "),input("Enter destination vertex: "))
    else:
        print("Terminating...")
        break
