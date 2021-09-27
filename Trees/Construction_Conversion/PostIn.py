pst_index=0
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root=None):
        self.root=root

    def inorder(self):
        if self.root==None:
            return

        self.inorder_helper(self.root)
        print()

    def inorder_helper(self,node):
        if node==None:
            return

        print(node.val,end='\t')
        self.inorder_helper(node.left)
        self.inorder_helper(node.right)

def create_Tree(pst,ino):
    global pst_index

    if len(pst)!=len(ino):
        return -1

    ht={ino[i]:i for i in range(len(ino))}
    pst_index=len(pst)-1
    start=0
    end=len(pst)-1

    print(ht)

    root=func(pst,ino,start,end,ht)
    t=Tree(root)
    t.inorder()
    
def func(pst,ino,start,end,ht):
    global pst_index

    if start>end:
        return

    node=Node(pst[pst_index])
    pst_index-=1   

    if start==end:
        return node

    in_index=ht[pst[pst_index+1]]

    node.right=func(pst,ino,in_index+1,end,ht)
    node.left=func(pst,ino,start,in_index-1,ht)

    return node

ino = [ 4, 8, 2, 5, 1, 6, 3, 7 ]
pst = [ 8, 4, 5, 2, 6, 7, 3, 1 ]
create_Tree(pst,ino)