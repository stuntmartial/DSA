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
	def rev_groups(self,k):
		if self.nodes==0:
			print("No nodes")
			return 

		ll=self.rev_groups_helper(self.head,k)

		disp2(ll)

	def rev_groups_helper(self,head,k):
		prev=None
		curr=head
		bkp=None
		count=0

		while count<k and curr!=None:
			bkp=curr.nxt_ptr
			curr.nxt_ptr=prev
			prev=curr
			curr=bkp
			count+=1

		if bkp != None:
			head.nxt_ptr=bkp
		count=0
		while curr!=None and count<k:
			curr=curr.nxt_ptr
			count+=1

		if curr!=None:
			curr.nxt_ptr=self.rev_groups_helper(curr.nxt_ptr,k)

		return prev
		
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

def disp2(node):

	l=[]
	ptr=node
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
		ll.rev_groups(int(input("Enter k : ")))
		ll.disp()

	else:
		print("Terminating...")
		break

'''

ll.add_beg(Node(1))
ll.add_end(Node(2))
ll.add_end(Node(3))
ll.add_end(Node(4))
ll.add_end(Node(5))
ll.add_end(Node(6))
ll.add_end(Node(7))
ll.add_end(Node(8))
ll.add_end(Node(9))
ll.disp()
ll.rev_groups(5)
