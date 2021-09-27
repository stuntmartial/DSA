class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def dfs(self):
        if self.root==None:
            return

        op=[]
        self.dfs_helper(self.root,op)
        print(op)
        return op

    def dfs_helper(self,node,op):
        if node==None:
            return

        self.dfs_helper(node.left,op)
        self.dfs_helper(node.right,op)
        op.append(node.val)

    def mps(self):
        if self.root==None or (self.root.left==None or self.root.right==None):
            return

        op=[-99999999999999]
        self.mps_helper(self.root,op)
        print(op[0])
        return op[0]

    def mps_helper(self,node,op):
        if node==None:
            return 0

        if node.left==None and node.right==None:
            return node.val

        lh=self.mps_helper(node.left,op)
        rh=self.mps_helper(node.right,op)

        if node.left !=None and node.right!=None:
            op[0]=max(op[0],node.val+lh+rh)
            return node.val+max(lh,rh)

        elif node.left!=None:
            return node.val+lh
        
        elif node.right!=None:
            return node.val+rh

root = Node(-15) 
root.left = Node(5) 
root.right = Node(6) 
root.left.left = Node(-8) 
root.left.right = Node(1) 
root.left.left.left = Node(2) 
root.left.left.right = Node(6) 
root.right.left = Node(3) 
root.right.right = Node(9) 
root.right.right.right= Node(0) 
root.right.right.right.left = Node(4) 
root.right.right.right.right = Node(-1) 
root.right.right.right.right.left = Node(10) 

t=Tree(root)
t.mps()

root=Node(-9)
root.left=Node(6)
root.right=Node(-10)
t2=Tree(root)
t2.mps()