class Node:

	def __init__(self,val = -1 , left = None , right = None):
		
		self.val = val
		
		if left != None:
			self.left = Node(left)
		else:
			self.left = None

		if right != None:
			
