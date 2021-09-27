ht={0:'A',1:'B',2:'C',3:'D',4:'E',5:'A',6:'B',7:'C',8:'D',9:'E'}
class PetersonGraph:
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

	def chk_path(self,s):
		



