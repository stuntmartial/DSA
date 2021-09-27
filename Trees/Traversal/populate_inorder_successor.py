class Node:
    def __init__(self,val,left=None,right=None,nxt=None):
        self.val=val
        self.left=left
        self.right=right
        self.nxt=nxt

class Tree:
    def __init__(self,root):
        self.root=root

    def inorder(self):
        if self.root==None:
            return

        visited=[]
        self.func(self.root,visited)
        for i in visited:
            if i.nxt!=None:
                print(i.val,'.nxt-->',i.nxt.val)
            else:
                print(i.val,'.nxt-->',i.nxt)

    def func(self,node,visited):
        if node==None:
            return 

        if len(visited)!=0:
            visited[len(visited)-1].nxt=node
            
        visited.append(node)
        self.func(node.left,visited)
        self.func(node.right,visited)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.left=Node(7)

t=Tree(root)
t.inorder()
        