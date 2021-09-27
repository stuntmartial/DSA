class Node:
	def __init__(self,val):
		self.val=val
		self.nxt_ptr=None

class Singly_ll:
	def __init__(self,head_node=None):
		self.head=head_node
		if self.head==None:
			self.nodes=0
		else:
			self.nodes=1

	def ins_at_beg(self,node):
		temp=self.head
		self.head=node
		self.head.nxt_ptr=temp
		self.nodes+=1

	def ins_at_end(self,node):
		ptr=self.head
		while ptr.nxt_ptr!=None:
			ptr=ptr.nxt_ptr

		ptr.nxt_ptr=node
		self.nodes+=1

	def sort012_func(self):
		Zero_ll=Singly_ll()
		One_ll=Singly_ll()
		Two_ll=Singly_ll()
		Zero_ll.ins_at_beg(Node(0))
		One_ll.ins_at_beg(Node(0))
		Two_ll.ins_at_beg(Node(0))
		Zero_ll.disp()
		One_ll.disp()
		Two_ll.disp()



		ptr=self.head

		while ptr!=None:
			if ptr.val==0:
				temp=ptr.nxt_ptr
				ptr.nxt_ptr=None
				Zero_ll.ins_at_end(ptr)
			elif ptr.val==1:
				temp=ptr.nxt_ptr
				ptr.nxt_ptr=None
				One_ll.ins_at_end(ptr)
			elif ptr.val==2:
				temp=ptr.nxt_ptr
				ptr.nxt_ptr=None
				Two_ll.ins_at_end(ptr)

			print("Worked on...",ptr.val)
			
			
			ptr=temp

		print("Loop ends...")

		self.head=Zero_ll.head.nxt_ptr
		self.ins_at_end(One_ll.head.nxt_ptr)
		self.ins_at_end(Two_ll.head.nxt_ptr)

		self.disp()


	def disp(self):
		ptr=self.head
		while ptr!=None:
			print(ptr.val," ",end="")
			ptr=ptr.nxt_ptr

		print()

ll=Singly_ll()

while True:
	
	ch=int(input("Enter choice : "))
	
	if ch==1:	
		val=int(input("Enter node val : "))
		node=Node(val)
		ll.ins_at_beg(node)
		ll.disp()

	elif ch==2:
		val=int(input("Enter node val : "))
		node=Node(val)
		ll.ins_at_end(node)
		ll.disp()

	elif ch==3:
		ll.sort012_func()

	elif ch==4:
		ll.disp()

	else:
		print("Terminating...")
		break
