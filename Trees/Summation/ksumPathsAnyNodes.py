class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def paths(self,k):
        if self.root==None:
            return

        path=[]
        self.func(self.root,path,k)

    def func(self,node,path,k):
        if node==None:
            return

        path.append(node.val)
        self.func(node.left,path,k)
        self.func(node.right,path,k)

        s=0
        for i in range(len(path)-1,-1,-1):
            s+=path[i]
            if s==k:
                #print(path)
                print_path(path,i)
                

        path.pop(-1)

def print_path(path,i):
    for j in range(i,len(path)):
        print(path[j],end='\t')

    print()

root = Node(1)  
root.left = Node(3)  
root.left.left = Node(2)  
root.left.right = Node(1)  
root.left.right.left = Node(1)  
root.right = Node(-1)  
root.right.left = Node(4)  
root.right.left.left = Node(1)  
root.right.left.right = Node(2)  
root.right.right = Node(5)  
root.right.right.right = Node(2)  
  
k = 5 
t=Tree(root)
t.paths(k)