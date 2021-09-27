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
        ptr=self.head
        if self.head==None:
            self.head=node
            node.nxt=self.head
            return

        while ptr.nxt!=self.head:
            ptr=ptr.nxt

        ptr.nxt=node
        node.nxt=self.head
        self.head=node

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

        print(ptr.nxt.val)
        print(node.nxt.val)

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

    def split(self):
        sp=fp=self.head
        while True:
            if fp.nxt==self.head or fp.nxt.nxt==self.head:
                break

            print(sp.val)
            sp=sp.nxt
            fp=fp.nxt.nxt

        if fp.nxt.nxt==self.head:
            fp=fp.nxt

        print('sp---->',sp.val)
        print('fp---->',fp.val)
        nxt_head=sp.nxt
        sp.nxt=self.head
        cll1=Cll();cll2=Cll()

        cll1.head=self.head
        cll2.head=nxt_head
        fp.nxt=nxt_head

        cll1.disp()
        cll2.disp()

        
ll=Cll()
'''
while True:
    ch=int(input("Enter choice : "))

    if ch==1:
        node_val=int(input("Enter node val :"))
        ll.add_beg(node_val)
        ll.disp()

    elif ch==2:
        node_val=int(input("Enter node val : "))
        ll.add_end(node_val)
        ll.disp()

    elif ch==3:
        ll.split()

    else:
        print("Terminating...")
        break
'''
ll.add_beg(1)
ll.add_end(2)
ll.add_end(3)
ll.add_end(4)
ll.add_end(5)
ll.add_end(6)

ll.disp()
ll.split()
