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

	def ins_at_middle(self,node,pos):
		i=0
		ptr=self.head
		while i<pos-1:
			ptr=ptr.nxt_ptr
			i+=1

		temp=ptr.nxt_ptr
		ptr.nxt_ptr=node
		node.nxt_ptr=temp
		self.nodes+=1

	def ins_at_end(self,node):
		ptr=self.head
		while ptr.nxt_ptr!=None:
			ptr=ptr.nxt_ptr

		ptr.nxt_ptr=node
		self.nodes+=1

	def del_beg(self):
		temp=self.head
		self.head=self.head.nxt_ptr
		print(temp.val," removed")

	def del_mid(self,pos):
		ptr=self.head
		prev_node=None
		i=0
		while i<pos-1:
			prev_node=ptr
			ptr=ptr.nxt_ptr
			i+=1

		print(i)
		print(prev_node.val)
		print(ptr.val)
		prev_node.nxt_ptr=ptr.nxt_ptr
		ptr.nxt_ptr=None
		print(ptr.val," deleted")

	def del_end(self):
		ptr=self.head
		prev_node=None
		while ptr.nxt_ptr!=None:
			prev_node=ptr
			ptr=ptr.nxt_ptr

		prev_node.nxt_ptr=None
		print(ptr.val," is deleted")

	def disp(self):
		ptr=self.head
		l=[]
		while ptr!=None:
			l.append(ptr.val)
			ptr=ptr.nxt_ptr
		print(l)

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
		pos=int(input("Enter pos : "))
		node=Node(val)
		ll.ins_at_middle(node,pos)
		ll.disp()

	elif ch==3:
		val=int(input("Enter node val : "))
		node=Node(val)
		ll.ins_at_end(node)
		ll.disp()
		 
	elif ch==4:
		ll.del_beg()
		ll.disp()

	elif ch==5:
		pos=int(input("Enter node pos : "))
		ll.del_mid(pos)
		ll.disp()
	
	elif ch==6:
		ll.del_end()
		ll.disp()
	


