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

    def get_diameter(self):
        if self.root==None:
            return

        op=[0]
        self.get_diameter_helper(self.root,op)
        print("Number of nodes in diamter is :",op[0])
        return op[0]

    def get_diameter_helper(self,node,op):
        if node==None:
            return 0

        lh=self.get_diameter_helper(node.left,op)
        rh=self.get_diameter_helper(node.right,op)

        op[0]=max(op[0],1+lh+rh)

        return 1+max(lh,rh)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

t=Tree(root)
t.get_diameter()