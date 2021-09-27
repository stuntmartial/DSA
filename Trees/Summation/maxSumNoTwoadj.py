class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def find_maxSum(self):
        if self.root==None:
            return

        dp={}
        self.func(self.root,dp)
        for i in dp:
            print(i.val," : ",dp[i])
        return dp[self.root]

    def func(self,node,dp):
        if node==None:
            return 0

        if node in dp.keys():
            return dp[node]

        inc=node.val

        if node.left!=None:
            inc+=self.func(node.left.left,dp)
            inc+=self.func(node.left.right,dp)

        if node.right!=None:
            inc+=self.func(node.right.left,dp)
            inc+=self.func(node.right.right,dp)

        exc=self.func(node.left,dp)+self.func(node.right,dp)
        dp[node]=max(inc,exc)

        return dp[node]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.left.left = Node(1)

t=Tree(root)
t.find_maxSum()