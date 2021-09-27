class Node:
    def __init__(self,val,left=None,right=None,nxt=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def modify(self):
        if self.root==None:
            return

        self.func(self.root)
        

    def func(self,node):
        
        if node==None:
            print(node)
        else:
            print(node.val)

        right=node.right
        rightmost=node

        if node.left!=None:
            rightmost=self.func(node.left)
            node.right=node.left
            node.left=None

        if right==None:
            return rightmost    
        
        rightmost.right=right

        rightmost=self.func(right)
        return rightmost

root = Node(10)  
root.left = Node(8)  
root.right = Node(2)  
root.left.left = Node(3)  
root.left.right = Node(5)  

t=Tree(root)
t.modify()
print(root.val)
print(root.right.val)
print(root.right.right.val)
print(root.right.right.right.val)
print(root.right.right.right.right.val)

        