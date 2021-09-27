op=[]
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root

    def inorder(self):
        if self.root==None:
            return

        inord=[]
        self.inorder_helper(self.root,inord)
        return inord

    def inorder_helper(self,node,inord):
        if node==None:
            return

        self.inorder_helper(node.left,inord)
        inord.append(node.val)
        self.inorder_helper(node.right,inord)

def merge(bst1,bst2):
    global op
    if bst1==None:
        return bst2.inorder()

    elif bst2==None:
        return bst1.inorder()

    c1=bst1.root;c2=bst2.root
    s1=[];s2=[]
    op=[]

    while s1 or s2 or c1 or c2:
    
        if c1 or c2:
            if c1:
                s1.append(c1)
                c1=c1.left
            if c2:
                s2.append(c2)
                c2=c2.left

        else:
            if not s1:
                while s2:
                    c2=s2.pop(len(s2)-1)
                    c2.left=None
                    k=[]
                    bst2.inorder_helper(c2,k)
                    for j in k:
                        op.append(j)
                return op
            if not s2:  
                while s1:
                    c1=s1.pop(len(s1)-1)
                    c1.left=None
                    k=[]
                    bst1.inorder_helper(c1,k)
                    for j in k:
                        op.append(j)
                return op
            
            c1=s1.pop(len(s1)-1)
            c2=s2.pop(len(s2)-1)

            if c1.val<=c2.val:
                op.append(c1.val)
                c1=c1.right
                s2.append(c2)
                c2=None

            elif c2.val<c1.val:
                op.append(c2.val)
                c2=c2.right
                s1.append(c1)
                c1=None
        

root1=Node(30)
root1.left=Node(17)
root1.left.left=Node(15)
root1.left.right=Node(20)
root1.right=Node(40)
bst1=BST(root1)

root2=Node(24)
root2.left=Node(16)
root2.left.right=Node(18)
root2.left.right.left=Node(17)
root2.right=Node(29)
root2.right.right=Node(30)
root2.right.right.right=Node(40)
bst2=BST(root2)

l=merge(bst1,bst2)
print(op)