class Node:
	def __init__(self,val=None,nxt_ptr=None):
		self.val=val
		self.nxt_ptr=nxt_ptr

class LinkedList:

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

	def chk_pal(self):
		n=self.count_nodes()
		if n%2==0:
			fp=self.head
			sp=self.head
			prev=None
			while True:
				if fp.nxt_ptr.nxt_ptr==None:
					fp=fp.nxt_ptr
					prev=sp
					sp=sp.nxt_ptr
					mid_ele1=prev
					mid_ele2=sp
					last_ele=fp
					break
				else:
					fp=fp.nxt_ptr.nxt_ptr
					prev=sp
					sp=sp.nxt_ptr

			ll1=self.clone_ll(self.head,mid_ele1)
			print("ll1--->")
			ll1.disp()
			ll2=self.clone_ll(mid_ele2,fp)
			ll2=self.reverse(ll2)
			print("ll2--->")
			ll2.disp()

			flag=self.chk_pal_helper(ll1,ll2)
			print(flag)

		else:
			fp=self.head
			sp=self.head
			while fp.nxt_ptr!=None:
				fp=fp.nxt_ptr.nxt_ptr
				prev=sp
				sp=sp.nxt_ptr
			mid_ele=sp
			last_ele=fp
			
			ll1=self.clone_ll(self.head,prev)
			print("ll1--->")
			ll1.disp()
			ll2=self.clone_ll(sp.nxt_ptr,last_ele)
			ll2=self.reverse(ll2)
			print("ll2--->")
			ll2.disp()

			flag=self.chk_pal_helper(ll1,ll2)
			print(flag)

	def clone_ll(self,start,end):
		list_of_nodes=[]
		ptr=start		
		while True:
			node=Node(ptr.val,None)
			print(node.val)
			list_of_nodes.append(node)
			ptr=ptr.nxt_ptr
			if ptr==None: 
				break
			elif ptr==end.nxt_ptr:
				break

		ll=LinkedList(list_of_nodes[0])
		for i in range(1,len(list_of_nodes)):
			ll.ins_at_end(list_of_nodes[i])

		return ll

	def reverse(self,ll):
		print("Reversing....")
		ll.disp()
		ptr=ll.head
		list_of_nodes=[]
		while ptr!=None:
			node=Node(ptr.val,None)
			list_of_nodes.append(node)
			ptr=ptr.nxt_ptr

		rev_ll=LinkedList(list_of_nodes[len(list_of_nodes)-1])
		for i in range(len(list_of_nodes)-2,-1,-1):
			rev_ll.ins_at_end(list_of_nodes[i])

		rev_ll.disp()
		return rev_ll

	def chk_pal_helper(self,ll1,ll2):
		ptr1=ll1.head
		ptr2=ll2.head
		flag=1
		while True:
			if ptr1.val!=ptr2.val:
				flag=0
				break

			ptr1=ptr1.nxt_ptr
			ptr2=ptr2.nxt_ptr
			if ptr1!=None:
				if ptr2!=None:
					break
				else:
					flag=0
					break

			if ptr2!=None:
				if ptr1!=None:
					break
				else:
					flag=0
					break

		return flag

	def disp(self):
		ptr=self.head
		while ptr!=None:
			print(ptr.val," ",end=" ")
			ptr=ptr.nxt_ptr
		print()

	def count_nodes(self):
		ptr=self.head
		count=0
		while ptr!=None:
			count+=1
			ptr=ptr.nxt_ptr
		return count


ll=LinkedList()

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
		ll.disp()

	elif ch==4:
		ll.chk_pal()

	else:
		print("Terminating...")
		break