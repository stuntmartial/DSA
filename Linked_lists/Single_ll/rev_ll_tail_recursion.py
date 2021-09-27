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

	def reverse(self):
		if self.nodes==0:
			print("No nodes")
			return

		self.reverse_helper(None,self.head)
		self.disp()

	def disp(self):
		if self.nodes==0:
			print("No nodes")
			return

		l=[]
		ptr=self.head
		while ptr!=None:
			l.append(ptr.val)
			ptr=ptr.nxt_ptr

		print(l)
		return

	def reverse_helper(self,prev,curr):

		if curr.nxt_ptr==None:
			self.head=curr
			curr.nxt_ptr=prev
			return

		nxt=curr.nxt_ptr
		curr.nxt_ptr=prev
		self.reverse_helper(curr,nxt)

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
		ll.reverse()
		ll.disp()

	else:
		print("Terminating...")
		break
