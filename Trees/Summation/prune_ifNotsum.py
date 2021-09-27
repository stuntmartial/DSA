class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def prune(self,s):
        if self.root==None:
            return

        ht={}
        self.prune_helper(self.root,s,ht)
        print(ht)

    def prune_helper(self,node,s,ht):
        if node==None:
            return s

        if s-node.val<=0:
            ht[node.val]='NP'
            return s-node.val

        ls=self.prune_helper(node.left,s-node.val,ht)
        rs=self.prune_helper(node.right,s-node.val,ht)

        if ls<=0 or rs<=0:
            ht[node.val]='NP'
            return 0
        
        else:
            ht[node.val]='P'
            return min(ls,rs)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.left.left.left = Node(8) 
root.left.left.right = Node(9) 
root.left.right.left = Node(12) 
root.right.right.left = Node(10) 
root.right.right.left.right = Node(11) 
root.left.left.right.left = Node(13) 
root.left.left.right.right = Node(14) 
root.left.left.right.right.left = Node(15)

t=Tree(root)
t.prune(45)