class Node:
    def __init__(self,val,left=None,right=None,nxt=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def rev(self):
        if self.root==None:
            return

        self.func(self.root.left,self.root.right,0)
        self.inorder(self.root)

    def inorder(self,node):
        if node==None:
            return

        self.inorder(node.left)
        print(node.val,end=' ')
        self.inorder(node.right)
    
    def func(self,node1,node2,level):
        if node1==node2==None:
            return

        if level%2==0:
            node1.val,node2.val=node2.val,node1.val

        self.func(node1.left,node2.right,level+1)
        self.func(node1.right,node2.left,level+1)

if __name__ == '__main__':  
    root = Node('a') 
    root.left = Node('b') 
    root.right = Node('c') 
    root.left.left = Node('d') 
    root.left.right = Node('e') 
    root.right.left = Node('f') 
    root.right.right = Node('g') 
    root.left.left.left = Node('h') 
    root.left.left.right = Node('i') 
    root.left.right.left = Node('j') 
    root.left.right.right = Node('k') 
    root.right.left.left = Node('l') 
    root.right.left.right = Node('m') 
    root.right.right.left = Node('n') 
    root.right.right.right = Node('o') 

    t=Tree(root)
    t.inorder(t.root)
    print()
    t.rev()