index=0
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root

    def get_ksmallest(self,k):
        global index
        if self.root==None:
            return

        index=-1
        self.func(self.root,k)
    
    def func(self,node,k):
        global index

        if node==None:
            return

        self.func(node.left,k)
        index+=1
        if index==k:
            print(node.val)

        self.func(node.right,k)

root=Node(50)
root.left=Node(40)
root.left.right=Node(45)
root.left.right.left=Node(43)
root.right=Node(60)
root.right.left=Node(55)
root.right.left.right=Node(57)
root.right.right=Node(66)
t=BST(root)
t.get_ksmallest(3)