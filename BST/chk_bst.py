class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root

def chk_bst(t):
    if t.root==None:
        print('True')
        return

    lower_lim=-999999
    upper_lim=+999999

    flag=[1]
    func(t.root,lower_lim,upper_lim,flag)
    if flag[0]==1:
        print('True')
    else:
        print('False')

def func(node,lower_lim,upper_lim,flag):
    if node==None:
        return

    if node.val>=lower_lim and node.val<=upper_lim:
        func(node.left,lower_lim,node.val,flag)
        func(node.right,node.val,upper_lim,flag)
        return

    else:
        flag[0]=0
        return

root=Node(50)
root.left=Node(40)
root.left.right=Node(45)
root.left.right.left=Node(43)
root.right=Node(60)
root.right.left=Node(55)
root.right.left.right=Node(57)
root.right.left.right.left=Node(30)
root.right.right=Node(66)
t=BST(root)
chk_bst(t)