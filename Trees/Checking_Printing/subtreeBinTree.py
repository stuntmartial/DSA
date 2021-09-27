class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

def chk(roo1,root2):
    if root1==None or root2==None:
        return

    flag=traverse(roo1,root2,root2)
    if flag==False:
        print('No')
    else:
        print('Yes')

def isEqual(node1,node2):
    if node1==None and node2==None:
        return True
    elif node1==None or node2==None:
        return False

    if node1.val==node2.val:
        if node1.left!=None and node2.left!=None:
            if node1.left.val==node2.left.val:
                if node1.right!=None and node2.right!=None:
                    if node1.right.val==node2.right.val:
                        return True
                    else:
                        return False
                elif node1.right==None and node2.right==None:
                    return True
            else:
                return False
        elif node1.left==None and node2.left==None:
            return True
    else:
        return False
    
def traverse(node1,node2,root2):
    if node1==None and node2==None:
        return True
    elif node1==None or node2==None:
        return False

    print('node1---> ',node1.val,' node2---> ',node2.val)
    if isEqual(node1,node2):
        if traverse(node1.left,node2.left,root2) and traverse(node1.right,node2.right,root2):
            return True

    else:
        print('Before node2---> ',node2.val)
        node2=root2
        print('After node2---> ',node2.val)
        if node1!=None and node2!=None:
            if traverse(node1.left,node2,root2) and traverse(node1.right,node2,root2):
                return True

        elif node1==None or node2==None:
            return False

root1=Node('x')
root1.left=Node('a')
root1.right=Node('b')
root1.left.left=Node('c')
root1.left.right=Node('e')
root1.left.right.right=Node('f')
root1.left.right.right.left=Node('g')
root1.right.right=Node('d')

root2=Node('a')
root2.left=Node('c')
root2.right=Node('e')
root2.right.left=Node('l')
root2.right.right=Node('f')

chk(root1,root2)