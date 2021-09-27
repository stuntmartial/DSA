class Node:
	def __init__(self,val,down=None,right=None):
		self.val=val
		self.down=down
		self.right=right

class LinkedList:
	def __init__(self,head_node=None):
		self.head=head_node
		self.node_list=[]
		if self.head==None:
			self.nodes=0
		else:
			self.nodes=1

	def flatten_depth(self):
		print("Entering flatten_depth")
		if self.head==None:
			print("No nodes")
			return

		op=[]
		print("Entering dfs_depth")
		self.dfs_depth(self.head,op)
		for i in op:
			print(i.val)

	def dfs_depth(self,node,op):

		if node==None:
			return

		op.append(node)
		if node.down != None:
			self.dfs_depth(node.down,op)
		if node.right !=None:
			self.dfs_depth(node.right,op)
			
	def flatten_breadth(self):
		if self.nodes==0:
			print("No nodes")
			return			
		op=[]
		print("Entering dfs_breadth")
		self.dfs_breadth(self.head,op)
		print(op)

	def dfs_breadth(self,node,op):

		if node==None:
			return

		op.append(node)
		if node.right != None:
			self.dfs_breadth(node.right,op)
		if node.down !=None:
			self.dfs_breadth(node.down,op)
