class Node:
	def __init__(self,val,nxt=None,arb=None):
		self.val=val
		self.nxt=nxt
		self.arb=arb

class LL:
	def __init__(self,head=None):
		self.head=head
		if self.head==None:
			self.nodes=0
		else:
			self.nodes=1

	def add_beg(self,node):
		node=Node(node)
		temp=self.head
		self.head=node
		self.head.nxt=temp
		self.nodes+=1		

	def add_end(self,node):
		if self.head==None:
			print("No nodes")
			return 

		ptr=self.head

		while ptr.nxt!=None:
			ptr=ptr.nxt

		ptr.nxt=Node(node)
		self.nodes+=1

	def add_arb(self,node,arb_node):
		if self.head==None:
			print("No nodes")
			return

		ptr=self.head
		node_ptr=None
		arb_ptr=None

		while ptr!=None:
			if ptr.val==node:
				node_ptr=ptr

			if ptr.val==arb_node:
				arb_ptr=ptr

			ptr=ptr.nxt

		if node_ptr==None or arb_ptr==None:
			print("Node not present")
			return
			
		node_ptr.arb=arb_ptr

	def clone_ll(self):
		if self.head==None:
			print("No nodes")
			return None

		ht={}
		ptr=self.head
		while ptr!=None:
			ht[ptr]=Node(ptr.val)
			ptr=ptr.nxt

		ptr=self.head
		while ptr!=None:
			print(ptr.val," ",ht[ptr].val)
			ptr=ptr.nxt

		cloned_ll=LL()
		cloned_ll.head=ht[ll.head]
		print(cloned_ll.head.val)

		ptr=self.head
		ptr2=cloned_ll.head
		while ptr!=None:
			if ptr.nxt!=None:
				ptr2.nxt=ht[ptr.nxt]
			else:
				ptr2.nxt=None
			if ptr.arb!=None:
				ptr2.arb=ht[ptr.arb]
			else:
				ptr2.arb=None
				
			ptr=ptr.nxt
			ptr2=ptr2.nxt
			print("Loop executed...")

		return cloned_ll.head

def disp(node):
	if node==None:
		print("No nodes")
		return

	ptr=node
	while ptr!=None:
		print(ptr.val,end=" ")
		if ptr.nxt!=None:
			print(ptr.nxt.val,end=" ")
		else:
			print(ptr.nxt,end=" ")
		if ptr.arb!=None:
			print(ptr.arb.val,end=" ")
		else:
			print(ptr.arb,end=" ")
		
		ptr=ptr.nxt
		print()

ll=LL()
'''
while True:
	
	ch=int(input("Enter choice : "))
	
	if ch==1:	
		val=int(input("Enter node val : "))
		ll.add_beg(val)
		disp(ll.head)

	elif ch==2:
		val=int(input("Enter node val : "))
		ll.add_end(val)
		disp(ll.head)

	elif ch==3:
		node=int(input("Enter node : "))
		arb_node=int(input("Enter arb_node : "))
		ll.add_arb(node,arb_node)
		disp(ll.head)

	elif ch==4:
		cloned_ll=ll.clone_ll()
		disp(cloned_ll.head)

	else:
		print("Terminating....")
		break
'''
ll.add_beg(1)
ll.add_end(2)
ll.add_end(3)
ll.add_end(4)
ll.add_end(5)
ll.add_arb(1,3)
ll.add_arb(3,5)
ll.add_arb(2,1)
ll.add_arb(4,3)
#ll.add_arb(5,2)
disp(ll.head)
ll2_head=ll.clone_ll()
disp(ll2_head)