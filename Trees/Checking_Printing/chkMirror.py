class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

def chk_mirror(root1,root2):
    
    print(func(root1,root2))

def func(node1,node2):
    print('node1---> ',disp(node1),'node2---> ',disp(node2))
    
    if node1==None and node2==None:
        return True

    elif node1==None or node2==None:
        return False

    if node1.val==node2.val:
        if func(node1.left,node2.right) and func(node1.right,node2.left):
            return True
        else:
            return False
    else:
        return False

def disp(node):
    if node==None:
        return None
    else:
        return node.val

root1 = Node(1) 
root2 = Node(1) 
  
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
  
root2.left = Node(3) 
root2.right = Node(2) 
root2.right.left = Node(5) 
root2.right.right = Node(4) 

chk_mirror(root1,root2)