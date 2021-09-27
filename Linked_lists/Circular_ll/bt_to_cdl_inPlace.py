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
            print(ptr.val," ",end="")
            ptr=ptr.right
        print(ptr.val,end="")
        print()
        
class binTree:
    def __init__(self,root):
        self.root=root

    def inorder(self):
        if self.root==None:
            print("No nodes...")
            return

        cdl1=self.inorder_helper(self.root)
        print()
        cdl1.disp()
    
    def inorder_helper(self,node):
        if node==None:
            print("Node-----> None")
            return None

        print("Node----->",node.val)
        new_node=Node(node.val)
        
        print("Working on left of ",node.val)
        cdl1=self.inorder_helper(node.left)
        if cdl1==None:
            cdl1=cdl()
            cdl1.add_beg(new_node)
        else:
            cdl1.add_end(new_node)

        print("cdl1--->")
        cdl1.disp()
        
        print("Working on right of ",node.val)
        cdl2=self.inorder_helper(node.right)   
        if cdl2!=None:
            print("cdl2---->")
            cdl2.disp()
        else:
            print("cdl2-----> None") 
        cdl1=merge_cdls(cdl1,cdl2)
        return cdl1

def convert_bt_to_cdl(bt):
    bt.inorder()

def merge_cdls(cdl1_head,cdl2_head):
    print("Inside merging....")
    if cdl1_head==None:
        if cdl2_head==None:
            return None 
        else:
            cdl2_head.disp()
            return cdl2_head
    
    elif cdl2_head==None:
        if cdl1_head==None:
            return None 
        else:
            cdl1_head.disp()
            return cdl1_head
    

    first_first_node=cdl1_head.head
    first_last_node=cdl1_head.head.left
    second_first_node=cdl2_head.head
    second_last_node=cdl2_head.head.left

    first_last_node.right=second_first_node
    second_first_node.left=first_last_node

    first_first_node.left=second_last_node
    second_last_node.right=first_first_node
    
    c=cdl(cdl1_head.head)
    c.disp()
    return c


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

print()


c2=cdl()
c2.add_beg(Node(2500))
c2.add_end(Node(1200))
c2.add_end(Node(3000))
c2.add_end(Node(1000))
c2.disp()
print()

merge_cdls(c1.head,c2.head)
'''