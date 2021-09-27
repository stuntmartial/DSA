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
        if self.root==None:
            return

        op=[0]
        self.mps_helper(self.root,op)
        print(op[0])
        return op[0]

    def mps_helper(self,node,op):
        if node==None:
            return 0

        lh=self.mps_helper(node.left,op)
        rh=self.mps_helper(node.right,op)

        op[0]=max(op[0],node.val,node.val+lh+rh,node.val+max(lh,rh))

        return max(node.val,node.val+max(lh,rh))

root = Node(10) 
root.left = Node(2) 
root.right   = Node(10)
root.left.left  = Node(20) 
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left   = Node(3) 
root.right.right.right  = Node(4)
t=Tree(root)
t.mps()