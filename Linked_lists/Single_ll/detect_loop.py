class Node:
	def __init__(self,val=None,nxt_ptr=None):
		self.val=val
		self.nxt_ptr=nxt_ptr

class linked_list:
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

	def disp(self):
		ptr=self.head
		while ptr!=None:
			print(ptr.val,end=" ")
			ptr=ptr.nxt_ptr
		print()

	def detect_loop(self):
		slow_ptr=self.head
		fast_ptr=self.head
		flag=0
		while True:
			if fast_ptr.nxt_ptr==None:
				break
			elif fast_ptr.nxt_ptr.nxt_ptr==None:
				break
			
			fast_ptr=fast_ptr.nxt_ptr.nxt_ptr
			slow_ptr=slow_ptr.nxt_ptr

			if fast_ptr==slow_ptr:
				flag=1
				print("Loop detected...")
				break

		if flag==0:
			print("No loop detected")



'''
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
		ll.detect_loop()
		
	else:
		print("Terminating...")
		break
'''

n6=Node(6)
n5=Node(5,n6)
n4=Node(4,n5)
n3=Node(3,n4)
n2=Node(2,n3)
n1=Node(1,n2)
#n6.nxt_ptr=n6
ll=linked_list(n1)
ll.detect_loop()


