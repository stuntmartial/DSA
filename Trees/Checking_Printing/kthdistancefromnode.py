class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def kth(self,target,k):
        if self.root==None:
            return
        
        oplist=[]
        self.func(self.root,target,k,oplist)
        for i in oplist:
            print(i.val)

    def func(self,node,target,k,oplist):
        if node==None:
            return -1

        if node.val==target:
            self.printkdown(node,k,oplist)
            return 1

        lk=self.func(node.left,target,k,oplist)
        rk=self.func(node.right,target,k,oplist)

        if lk==-1 and rk==-1:
            return -1

        elif lk==-1:
            if k-rk>0:
                self.printkdown(node.left,k-rk-1,oplist)
            elif k-rk==0:
                oplist.append(node)
            return 1+rk

        elif rk==-1:
            if k-lk>0:
                self.printkdown(node.right,k-lk-1,oplist)
            elif k-lk==0:
                oplist.append(node)
            return 1+lk

    def printkdown(self,node,k,oplist):
        if node==None:
            return

        if k==0:
            oplist.append(node)
            return

        self.printkdown(node.left,k-1,oplist)
        self.printkdown(node.right,k-1,oplist)

root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14)

t=Tree(root)
t.kth(20,1)
