class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def maxS(self):
        if self.root==None:
            return

        print(max(
            self.func(self.root),
            self.func(self.root.left)+self.func(self.root.right)
        ))

    def func(self,node):
        if node==None:
            return 0

        s=node.val
        
        if node.left!=None:
            s+=self.func(node.left.left)
            s+=self.func(node.left.right)
        if node.right!=None:
            s+=self.func(node.right.left)
            s+=self.func(node.right.right)

        return s

'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.left.right = Node(5)
root.right.left.right.left = Node(6)

t=Tree(root)
t.maxS()
'''

root2=Node(10000)
root2.left=Node(1)
root2.right=Node(2)
root2.left.left=Node(3)
root2.left.right=Node(4)
root2.left.left.left=Node(100)
root2.left.right.left=Node(200)
root2.right.left=Node(5)
root2.right.left.left=Node(300)

t2=Tree(root2)
t2.maxS()