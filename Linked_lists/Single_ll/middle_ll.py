class Node:
	def __init__(self,val=0,nxt_ptr=None):
		self.val=val
		self.nxt_ptr=nxt_ptr

class linked_list:
	def __init__(self,head=None):
		self.head=head
		if self.head==None:
			self.nodes=0
		else:
			self.nodes+=1

	def add_node_beg(self,node):
		temp=self.head
		self.head=node
		node.nxt_ptr=temp
		self.nodes+=1

	def add_node_end(self,node):
		ptr=self.head
		temp=ptr
		while ptr!=None:
			temp=ptr
			ptr=ptr.nxt_ptr

		temp.nxt_ptr=node
		self.nodes+=1

	def find_middle_node(self):
		ptr1=self.head
		ptr2=self.head
		op=[]
		while True:
			if ptr1.nxt_ptr==None:
				op=[ptr2.val]
				break
			elif ptr1.nxt_ptr.nxt_ptr==None:
				op=[ptr2.val,ptr2.nxt_ptr.val]
				break

			ptr1=ptr1.nxt_ptr.nxt_ptr
			ptr2=ptr2.nxt_ptr

		print(op)
		return op

	def disp(self):
		ptr=self.head
		while ptr!=None:
			print(ptr.val,end="  ")
			ptr=ptr.nxt_ptr

		print()

ll=linked_list()
while True:
	
	ch=int(input("Enter choice : "))
	
	if ch==1:	
		val=int(input("Enter node val : "))
		node=Node(val)
		ll.add_node_beg(node)
		ll.disp()

	elif ch==2:
		val=int(input("Enter node val : "))
		node=Node(val)
		ll.add_node_end(node)
		ll.disp()
		 
	elif ch==3:
		ll.disp()

	elif ch==4:
		ll.find_middle_node()
		ll.disp()
	
	else:
		print("Terminating...")
		break