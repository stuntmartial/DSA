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

	def del_beg(self):
		temp=self.head
		self.head=self.head.nxt_ptr
		print(temp.val," removed")

	def del_end(self):
		ptr=self.head
		prev_node=None
		while ptr.nxt_ptr!=None:
			prev_node=ptr
			ptr=ptr.nxt_ptr

		prev_node.nxt_ptr=None
		print(ptr.val," is deleted")

	def del_nth_node_from_end(self,n):
		ptr1=self.head
		ptr2=self.head
		ptr_prev=None
		ptr_next=None
		try:
			for i in range(n):
				ptr1=ptr1.nxt_ptr

		except:
			print("Not so many nodes")

		while ptr1.nxt_ptr!=None:
			ptr1=ptr1.nxt_ptr
			ptr_prev=ptr2
			ptr2=ptr2.nxt_ptr
			if ptr2!=None:
				ptr_next=ptr2.nxt_ptr

		print("ptr1--->",ptr1.val,"ptr2--->",ptr2.val,"ptr_prev--->",ptr_prev,"ptr_next--->",ptr_next)
		if ptr2==self.head:
			self.del_beg()
		elif ptr2.nxt_ptr==None:
			self.del_end()
		else:

			ptr_prev.nxt_ptr=ptr_next
			ptr2=None

		#self.disp()

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
		ll.del_nth_node_from_end(int(input("Enter n : ")))
		ll.disp()
	
	else:
		print("Terminating...")
		break