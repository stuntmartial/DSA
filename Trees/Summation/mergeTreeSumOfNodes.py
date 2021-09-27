class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def preorder(self,node):
        if node==None:
            return

        print(node.val,end='\t')
        self.preorder(node.left)
        self.preorder(node.right)

def merge(t1_root,t2_root):
    if t1_root == None or t2_root == None:
        return

    t3_root=func(t1_root,t2_root)
    return t3_root

def func(node1,node2):
    if node1==None and node2==None:
        return

    if node1==None:
        node3=Node(node2.val)
        node3.left=func(None,node2.left)
        node3.right=func(None,node2.right)
    elif node2==None:
        node3=Node(node1.val)
        node3.left=func(node1.left,None)
        node3.right=func(node1.right,None)
    else:
        node3=Node(node1.val+node2.val)
        node3.left=func(node1.left,node2.left)
        node3.right=func(node1.right,node2.right)

    return node3

    
root1 = Node(1) 
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
root1.right.right = Node(6)

root2 = Node(4) 
root2.left = Node(1) 
root2.right = Node(7) 
root2.left.left = Node(3) 
root2.right.left = Node(2) 
root2.right.right = Node(6) 
root2.right.right.left =Node(7)
root2.right.right.left.right=Node(9)

t1=Tree(root1)
t2=Tree(root2)
root3=merge(t1.root,t2.root)
t3=Tree(root3)
t3.preorder(t3.root)
'''
print()
print(t3.root.right.right.left.val)
print(t3.root.right.right.left.right.val)
'''