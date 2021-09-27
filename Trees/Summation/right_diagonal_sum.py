class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def rds(self):
        ht={}
        val_dict={self.root:0}
        self.rds_helper(root,ht,val_dict)
        print(ht)

    def rds_helper(self,node,ht,val_dict):
        if node==None:
            return

        try:
            ht[val_dict[node]]+=node.val
        except:
            ht[val_dict[node]]=node.val

        if node.left!=None:
            val_dict[node.left]=val_dict[node]+1
        if node.right!=None:
            val_dict[node.right]=val_dict[node]

        self.rds_helper(node.left,ht,val_dict)
        self.rds_helper(node.right,ht,val_dict)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
             
Tree(root).rds()