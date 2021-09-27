class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root

def chk_dead_end(t):
    if t.root==None:
        print('True')
        return

    lower_lim=-999999
    upper_lim=+999999

    flag=[1]
    func(t.root,lower_lim,upper_lim,flag)
    if flag[0]==1:
        print('Dead end not present')
    else:
        print('Dead end present')

def func(node,lower_lim,upper_lim,flag):
    if node==None:
        return

    if node.left==None and node.right==None:
        if lower_lim==upper_lim:
            flag[0]=0
            return

    func(node.left,lower_lim,node.val-1,flag)
    func(node.right,node.val+1,upper_lim,flag)

root=Node(50)
root.left=Node(40)
root.left.right=Node(45)
root.left.right.left=Node(43)
root.right=Node(60)
root.right.left=Node(55)
root.right.left.right=Node(57)
root.right.left.right.left=Node(56)
root.right.right=Node(66)
t=BST(root)
chk_dead_end(t)