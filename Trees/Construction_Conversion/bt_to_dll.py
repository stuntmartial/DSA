head=None
tail=None
count=0
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def convert_to_ll(self):
        global head,tail,count
        if self.root==None:
            return

        self.func(self.root)
        ptr=head
        while ptr!=None:
            print(ptr.val,end='')
            ptr=ptr.right

    def func(self,node):
        global head,tail,count

        if node==None:
            return None

        self.func(node.left)

        if head==None:
            head=node
            tail=node

        else:
            tail.right=node
            node.left=tail
            tail=node
        
        count+=1

        self.func(node.right)

root = Node(5) 
root.left = Node(3) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.right.right = Node(8) 
root.left.left.left = Node(0) 
root.left.left.right = Node(2) 
root.right.right.left = Node(7) 
root.right.right.right = Node(9)

tree=Tree(root) 
tree.convert_to_ll()