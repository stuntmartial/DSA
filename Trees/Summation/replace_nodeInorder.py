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

        inord=[]
        self.func(self.root,inord)
        return inord

    def func(self,node,inord):
        if node==None:
            return

        self.func(node.left,inord)
        inord.append(node.val)
        self.func(node.right,inord)

    def repl(self):
        inord=self.inorder()
        print(inord)
        inord.insert(0,0)
        inord.append(0)
        ht={}
        for i in range(1,len(inord)-1):
            ht[inord[i]]=inord[i-1]+inord[i+1]

        print(ht)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)  
root.left.right = Node(5)   
root.right.left = Node(6)  
root.right.right = Node(7)
t=Tree(root)
t.repl()