class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def count_nodes(self):
        if self.root==None:
            return

        count=[0]
        self.count_helper(self.root,count)
        return count[0]

    def count_helper(self,node,count):
        if node==None:
            return

        count[0]+=1
        self.count_helper(node.left,count)
        self.count_helper(node.right,count)

    def chk_halves(self):
        if self.root==None:
            return

        flag=[0]
        n=self.count_nodes()
        self.func(self.root,flag,n)
        if flag[0]==1:
            print('Yes')
        else:
            print('No')

    def func(self,node,flag,n):
        if node==None:
            return 0
        
        ls=self.func(node.left,flag,n)
        rs=self.func(node.right,flag,n)

        subtree_length=1+ls+rs
        if subtree_length==n-subtree_length:
            flag[0]=1
            
        return subtree_length

root = Node(5) 
root.left = Node(1) 
root.right = Node(6) 
root.left.left = Node(3) 
root.right.left = Node(7) 
root.right.right = Node(4)
root.right.right.left = Node(11)

t=Tree(root)
t.chk_halves()