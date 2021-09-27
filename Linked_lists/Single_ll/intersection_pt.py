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

def find_intersecting_pt(l1,l2):
	ptr1=l1.head
	ptr2=l2.head

	while True:
		if ptr1!=None:
			ptr1=ptr1.nxt_ptr
		else:
			ptr1=l2.head

		if ptr2!=None:
			ptr2=ptr2.nxt_ptr 
		else:
			ptr2=l1.head

		if ptr1==ptr2:
			if ptr1==None:
				print("No intersecting_pt...")
			else:
				print(ptr1.val)

			return

l1=LinkedList()
l2=LinkedList()

inst=Node(15)
l1.add_beg(Node(3))
l1.add_end(Node(6))
l1.add_end(Node(9))
l1.add_end(inst)
l1.add_end(Node(30))

n1=Node(10)
l2.add_beg(Node(6))
l2.add_end(n1)
n1.nxt_ptr=inst

l1.disp()
l2.disp()

find_intersecting_pt(l1,l2)

