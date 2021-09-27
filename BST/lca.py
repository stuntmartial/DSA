class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root

    def get_lca(self,node1,node2):
        if self.root==None:
            return

        self.func(self.root,node1,node2)

    def func(self,node,node1,node2):
        if node==None:
            return

        if (node1<=node.val and node2>=node.val) or (node1>=node.val and node2<=node.val):
            
            print(node.val)
            return

        elif node1<=node.val and node2<=node.val:
            self.func(node.left,node1,node2)
        
        elif node1>=node.val and node>=node.val:
            self.func(node.right,node1,node2)
    
root=Node(50)
root.left=Node(40)
root.left.right=Node(45)
root.left.right.left=Node(43)
root.right=Node(60)
root.right.left=Node(55)
root.right.left.right=Node(57)
root.right.right=Node(66)
t=BST(root)
t.get_lca(40,60)