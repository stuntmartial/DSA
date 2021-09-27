class Node:
    def __init__(self,val,nxt=None):
        self.val=val
        self.nxt=nxt

class Cll:
    def __init__(self,head=None):
        self.head=head
        if self.head==None:
            self.nodes=0
        else:
            self.nodes=1

    def add_beg(self,node_val):
        node=Node(node_val)
        temp=self.head
        self.head=node
        node.nxt=temp
        self.nodes+=1

    def add_end(self,node_val):
        if self.head==None:
            print("No nodes")
            return

        ptr=self.head
        while True:
            if ptr.nxt!=self.head:
                ptr=ptr.nxt
            else:
                break

        node=Node(node_val)
        ptr.nxt=node
        node.nxt=self.head
        self.nodes+=1

    def disp(self):
        if self.head==None:
            print('None')
            return

        ptr=self.head
        l=[]
        while True:
            l.append(ptr.val)
            ptr=ptr.nxt
            if ptr.nxt==self.head:
                if ptr !=self.head:
                    l.append(ptr.val)
                break

        print(l)
        return

ll=Cll()

while True:
	
	ch=int(input("Enter choice : "))
	
	if ch==1:	
		node_val=int(input("Enter node val : "))
		ll.add_beg(node_val)
		ll.disp()

	elif ch==2:
		node_val=int(input("Enter node val : "))
		ll.add_end(node_val)
		ll.disp()
    