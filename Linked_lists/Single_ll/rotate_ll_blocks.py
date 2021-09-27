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

def rotate_blocks_left(head,k):
	if head==None:
		return None

	print(head.val)

	ptr=head
	fp=head
	count=1
	prev=None
	while count<k and ptr.nxt_ptr!=None:
		prev=ptr
		ptr=ptr.nxt_ptr
		count+=1
		
	if ptr!=None:
		temp=ptr.nxt_ptr
		ptr.nxt_ptr=head
		head=head.nxt_ptr
	
		fp.nxt_ptr=rotate_blocks_left(temp,k)	
	
	return head

def rotate_blocks_right(head,k):
	if head==None:
		return None

	print(head.val)

	ptr=head
	fp=head
	count=1
	prev=None
	while count<k and ptr.nxt_ptr!=None:
		print("Executing loop...")
		prev=ptr
		ptr=ptr.nxt_ptr
		count+=1
		
	if prev!=None:
		temp=ptr.nxt_ptr
		print("temp--->",temp)
		ptr.nxt_ptr=head
		head=ptr
		#print("head--->",head.val,head.nxt_ptr.val,head.nxt_ptr.nxt_ptr.val)

		prev.nxt_ptr=rotate_blocks_right(temp,k)	
	
	print("head during return.....",head.val)
	
	return head


l=LinkedList()
l.add_beg(Node(1))
l.add_end(Node(2))
l.add_end(Node(3))
l.add_end(Node(4))
l.add_end(Node(5))
l.add_end(Node(6))
l.add_end(Node(7))
l.add_end(Node(8))
l.add_end(Node(9))
l.add_end(Node(10))
#l.add_end(Node(11))

#l.add_end(Node(2))
'''
'''
l.disp()

ll_head=rotate_blocks_right(l.head,int(input("Enter k : ")))

ptr=ll_head
li=[]
while ptr!=None:
	li.append(ptr.val)
	ptr=ptr.nxt_ptr

print(li)