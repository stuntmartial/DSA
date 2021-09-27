class Node:
	def __init__(self,val,nxt_ptr=None):
		self.val=val
		self.nxt_ptr=nxt_ptr

class LinkedList:
	def __init__(self,head=None):
		self.head=head
		if self.head==None:
			self.nodes=0
		else:
			self.nodes=1

	def add_beg(self,node):
		temp=self.head
		self.head=node
		node.nxt_ptr=temp
		self.nodes+=1
		self.disp()

	def add_end(self,node):
		ptr=self.head
		while ptr.nxt_ptr!=None:
			ptr=ptr.nxt_ptr

		ptr.nxt_ptr=node
		self.nodes+=1

	def disp(self):
		if self.head==None:
			print("No nodes")
			return
		l=[]
		ptr=self.head
		while ptr!=None:
			l.append(ptr.val)
			ptr=ptr.nxt_ptr

		print(l)

	def rotate_right(self):
		if self.head==None:
			print("No nodes")
			return

		ptr=self.head
		prev=None
		while ptr.nxt_ptr!=None:
			prev=ptr
			ptr=ptr.nxt_ptr

		prev.nxt_ptr=None
		ptr.nxt_ptr=self.head
		self.head=ptr

		self.disp()

	def rotate_left(self):
		if self.head==None:
			print("No nodes")
			return

		ptr=self.head

		while ptr.nxt_ptr!=None:
			ptr=ptr.nxt_ptr

		temp=self.head
		self.head=self.head.nxt_ptr
		ptr.nxt_ptr=temp
		temp.nxt_ptr=None

		self.disp()


ll=LinkedList()
ll.add_beg(Node(1))
ll.add_end(Node(2))
ll.add_end(Node(3))
ll.add_end(Node(4))
ll.add_end(Node(5))

ll.disp()

ll.rotate_left()

ll.disp()

