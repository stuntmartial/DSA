pre_index=0
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

def create_Tree(pre,ino):
    global pre_index

    if len(pre)!=len(ino):
        return -1

    ht={ino[i]:i for i in range(len(ino))}
    pre_index=0
    start=0
    end=len(pre)-1

    print(ht)

    root=func(pre,ino,start,end,ht)
    t=Tree(root)
    t.inorder()
    
def func(pre,ino,start,end,ht):
    global pre_index

    if start>end:
        return

    node=Node(pre[pre_index])
    pre_index+=1   

    if start==end:
        return node

    in_index=ht[pre[pre_index-1]]

    node.left=func(pre,ino,start,in_index-1,ht)
    node.right=func(pre,ino,in_index+1,end,ht)

    return node

pre=['a','b','d','e','c','f']
ino=['d','b','e','a','f','c']

create_Tree(pre,ino)