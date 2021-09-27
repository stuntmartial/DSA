class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def count(self,node):
        if node==None:
            return 0

        return 1+self.count(node.left)+self.count(node.right)

    def chkcom(self):
        if self.root==None:
            return

        n=self.count(self.root)
        flag=self.func(self.root,0,n)
        print(flag)

    def func(self,node,index,n):
        if node==None:
            return True

        if index>=n:
            return False

        return self.func(node.left,2*index+1,n) and self.func(node.right,2*index+2,n)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 

t=Tree(root)
t.chkcom()