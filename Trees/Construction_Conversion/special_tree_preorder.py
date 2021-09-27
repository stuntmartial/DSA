pre_index=0
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def inorder(self):
        if self.root==None:
            return
        
        self.func(self.root)
        print()

    def func(self,node):
        if node==None:
            return

        self.func(node.left)
        print(node.val,end='\t')
        self.func(node.right)

def create_tree(pre,preln):
    global pre_index

    if len(pre)!=len(pre):
        return None

    start=0
    end=0
    pre_index=0
    root=utility(pre,preln,start,end)
    t=Tree(root)
    t.inorder()

def utility(pre,preln,start,end):
    global pre_index
    if start>end or pre_index>=len(pre):
        return None

    p=pre_index
    node=Node(pre[pre_index])
    pre_index+=1

    if start==end and pre_index>=len(pre):
        return node

    if preln[p]=='N':
        node.left=utility(pre,preln,start,end)
        node.right=utility(pre,preln,start,end)

    return node

pre=[10, 30, 20, 5, 15]
preln=['N', 'N', 'L', 'L', 'L']

create_tree(pre,preln)