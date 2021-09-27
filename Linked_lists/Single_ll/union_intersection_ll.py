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

def find_union(l1,l2):
	ht1={}
	ht2={}
	ht2_={}

	ptr1=l1.head
	while ptr1!=None:
		try:
			ht1[ptr1.val]+=1
		except:
			ht1[ptr1.val]=1
		ptr1=ptr1.nxt_ptr

	print(ht1)
	ptr2=l2.head
	while ptr2!=None:
		try:
			ht2[ptr2.val]+=1
		except:
			ht2[ptr2.val]=1
			ht2_[ptr2.val]='UM'

		ptr2=ptr2.nxt_ptr

	print(ht2)

	union_linkedlist=LinkedList()
	first_node=list(ht1.keys())[0]
	union_linkedlist.add_beg(Node(first_node))
	ht1[first_node]-=1
	if first_node in ht2.keys():
		ht2[first_node]-=1

	for i in range(len(list(ht1.keys()))):

		key=list(ht1.keys())[i]
		noht1=ht1[key]

		if key in ht2.keys():
			noht2=ht2[key]
			ht2_[key]='M'
		else:
			noht2=0

		res_no=max(noht1,noht2)
		for j in range(res_no):
			union_linkedlist.add_end(Node(key))

	for i in range(len(list(ht2.keys()))):

		key=list(ht2.keys())[i]
		if ht2_[key]=='M':
			continue
		else:
			res_no=ht2[key]
			for i in range(res_no):
				union_linkedlist.add_end(Node(key))
			ht2_[key]='M'

	union_linkedlist.disp()

def intersection(l1,l2):

	ht1={}
	ht2={}
	
	ptr1=l1.head
	while ptr1!=None:
		try:
			ht1[ptr1.val]+=1
		except:
			ht1[ptr1.val]=1
		ptr1=ptr1.nxt_ptr

	print(ht1)
	ptr2=l2.head
	while ptr2!=None:
		try:
			ht2[ptr2.val]+=1
		except:
			ht2[ptr2.val]=1

		ptr2=ptr2.nxt_ptr

	print(ht2)
	intersection_linkedlist=LinkedList()
	count=0
	for i in range(len(list(ht1.keys()))):

		key=list(ht1.keys())[i]

		if key not in ht2.keys():
			continue
		else:
			 res_no=min(ht1[key],ht2[key])
			 for j in range(res_no):
			 	if count==0:
			 		intersection_linkedlist.add_beg(Node(key))
			 	else:
			 		intersection_linkedlist.add_end(Node(key))
			 	count+=1

	intersection_linkedlist.disp()

ll1=LinkedList()
ll2=LinkedList()

ll1.add_beg(Node(1))
#ll1.disp()
ll2.add_beg(Node(1))
#ll2.disp()

ll1.add_end(Node(2))
ll1.add_end(Node(3))
ll1.add_end(Node(7))
ll1.add_end(Node(4))

print("Printing ll1...")
ll1.disp()

ll2.add_end(Node(1))
ll2.add_end(Node(3))
ll2.add_end(Node(8))
ll2.add_end(Node(9))

print("Printing ll2...")
ll2.disp()

find_union(ll1,ll2)
intersection(ll1,ll2)



	