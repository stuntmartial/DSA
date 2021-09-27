found=0
path_index=0
class Node:
    def __init__(self,val,left=None,right=None,nxt=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def inorder(self,node):
        if node==None:
            return

        self.inorder(node.left)
        print(node.val,end='\t')
        self.inorder(node.right)

    def rev_tree_path(self,data):
        global found,path_index

        if self.root==None:
            return

        if data==self.root.val:
            self.inorder()
            return

        found=0
        path_index=0
        path=[]
        self.func(self.root,path,data)
        if found==1:
            self.inorder(self.root)
             
    def func(self,node,path,data):
        global found,path_index

        if node==None:
            return

        path.append(node.val)
        print('node---> ',node.val,' path---> ',path)
        
        if node.val==data:
            print('GOT!!!!!!')
            found=1
            print('path_index ',path)
            node.val=path[path_index]
            #path.pop(len(path)-1)
            return

        self.func(node.left,path,data)
        if found==1:
            path_index+=1
            node.val=path[path_index]
            print(path_index)
            #path.pop(len(path)-1)
            print(path)
            return
        #path.pop(len(path)-1)
        
        self.func(node.right,path,data)
        if found==1:
            path_index+=1
            node.val=path[path_index]
            #path.pop(len(path)-1)
            return
        
        path.pop(len(path)-1)

root = Node(7)
root.left = Node(6)
root.right = Node(5)
root.left.left = Node(4)
root.left.left.right=Node(14)
root.left.right = Node(3)
root.right.left = Node(2)
root.right.right = Node(1)

t=Tree(root)
data=1
t.rev_tree_path(data)