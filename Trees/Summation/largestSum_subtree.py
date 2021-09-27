class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def lsSum(self):
        if self.root==None:
            return 

        s=[-999999]
        self.func(self.root,s)
        print(s[0])

    def func(self,node,s):
        if node==None:
            return 0

        s1=node.val+self.func(node.left,s)+self.func(node.right,s)
        s[0]=max(s[0],s1)

        return s1

root = Node(1)  
root.left = Node(-2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5)  
root.right.left = Node(-6)  
root.right.right = Node(2)  

t=Tree(root)
t.lsSum()