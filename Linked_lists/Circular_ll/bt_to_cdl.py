class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class cdl:
    def __init__(self,head=None):
        self.head=head
        if self.head==None:
            self.nodes=0
        else:
            self.nodes=1

    def add_beg(self,node):
        if self.head==None:
            self.head=node
            node.right=node
            node.left=node
        else:
            first_node=self.head
            last_node=self.head.left
            node.right=first_node
            node.left=last_node
            first_node.left=node 
            last_node.right=node
        
    def add_end(self,node):
        first_node=self.head
        last_node=self.head.left

        last_node.right=node
        node.left=last_node
        first_node.left=node
        node.right=first_node

    def disp(self):
        if self.head==None:
            print("No nodes...")
            return 

        ptr=self.head
        while ptr.right!=self.head:
            print(ptr.val," ",ptr.left.val," ",ptr.right.val)
            ptr=ptr.right
        print(ptr.val," ",ptr.left.val," ",ptr.right.val)
        
class binTree:
    def __init__(self,root):
        self.root=root

    def inorder(self):
        if self.root==None:
            print("No nodes...")
            return

        l=[]
        self.inorder_helper(self.root,l)
        print(l)
        return l
    
    def inorder_helper(self,node,l):
        if node==None:
            return

        self.inorder_helper(node.left,l)
        l.append(node.val)
        self.inorder_helper(node.right,l)

def convert_bt_to_cdl(bt):
    l=bt.inorder()
    cdl1=cdl()
    cdl1.add_beg(Node(l[0]))
    for i in range(0,len(l)):
        cdl1.add_end(Node(l[i]))

    cdl1.disp()

n1=Node(10)
n2=Node(12)
n3=Node(15)
n4=Node(25)
n5=Node(30)
n6=Node(36)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6

bt=binTree(n1)
convert_bt_to_cdl(bt)

'''
c1=cdl()
c1.add_beg(Node(25))
c1.add_end(Node(12))
c1.add_end(Node(30))
c1.add_end(Node(10))
c1.add_end(Node(36))
c1.add_end(Node(15))
c1.disp()
'''

 