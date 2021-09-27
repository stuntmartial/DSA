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

	def add_end(self,node):
		ptr=self.head
		while ptr.nxt_ptr!=None:
			ptr=ptr.nxt_ptr

		ptr.nxt_ptr=node
		self.nodes+=1

	def separate(self,head_node):
		if head_node==None or head_node.nxt_ptr==None:
			return head_node

		mid_ptr=self.find_mid(head_node)
		print(mid_ptr.val)
		mid_ptr_nxt_bkp=mid_ptr.nxt_ptr
		mid_ptr.nxt_ptr=None

		l=self.separate(head_node)
		disp(l)
		r=self.separate(mid_ptr_nxt_bkp)
		disp(r)
		sorted_arr=self.merge(l,r)
		return sorted_arr

	def merge(self,hn1,hn2):
		print("Entering merge...")
		disp(hn1)
		disp(hn2)

		if hn1==None:
			return hn2
		if hn2==None:
			return hn1

		res_head_ptr=None

		if hn1.val<=hn2.val:
			res_head_ptr=hn1
			res_head_ptr.nxt_ptr=self.merge(hn1.nxt_ptr,hn2)

		else:
			res_head_ptr=hn2
			res_head_ptr.nxt_ptr=self.merge(hn1,hn2.nxt_ptr)

		disp(res_head_ptr)
		return res_head_ptr

	def find_mid(self,head_node):
		if head_node==None:
			return None

		fp=head_node
		sp=head_node

		while fp.nxt_ptr!=None and fp.nxt_ptr.nxt_ptr!=None:
			fp=fp.nxt_ptr.nxt_ptr
			sp=sp.nxt_ptr

		return sp

def disp(head):
	if head==None:
		print("No nodes")
		return

	l=[]
	ptr=head
	while ptr!=None:
		l.append(ptr.val)
		ptr=ptr.nxt_ptr

	print(l)

ll=LinkedList()
'''
while True:
	
	ch=int(input("Enter choice : "))
	
	if ch==1:	
		val=int(input("Enter node val : "))
		node=Node(val)
		ll.add_beg(node)
		ll.disp()

	elif ch==2:
		val=int(input("Enter node val : "))
		node=Node(val)
		ll.add_end(node)
		ll.disp()

	elif ch==3:
		sorted_ll=ll.separate(ll.head)
		sorted_ll.disp()

	elif ch==4:
		ll.disp()

	else:
		print("Terminating...")
		break
'''
ll.add_beg(Node(3))
ll.add_end(Node(4))
ll.add_end(Node(1))
ll.add_end(Node(5))
ll.add_end(Node(2))
disp(ll.head)
l=ll.separate(ll.head)
disp(l)