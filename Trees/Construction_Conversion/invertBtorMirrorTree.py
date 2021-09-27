class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def invert_tree(self):
        if self.root==None:
            return -1

        self.func(self.root)
        self.inorder()
        print()

    def func(self,node):
        if node==None:
            return

        self.func(node.left)
        self.func(node.right)
        
        node.left,node.right=node.right,node.left

    def inorder(self):
        if self.root==None:
            return

        self.utility(self.root)
        print()

    def utility(self,node):
        if node==None:
            return

        self.utility(node.left)
        print(node.val,end='\t')
        self.utility(node.right)

root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5) 

t=Tree(root)
t.inorder()
t.invert_tree()