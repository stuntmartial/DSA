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
    if bst1==None:
        return root2

    elif bst2==None:
        return root1

    ino1=bst1.inorder()
    ino2=bst2.inorder()
    print(ino1,ino2)
    mrg_ino=[]
    index1=0;index2=0
    
    while index1 < len(ino1) and index2 < len(ino2):
        if ino1[index1]<ino2[index2]:
            mrg_ino.append(ino1[index1])
            index1+=1
        else:
            mrg_ino.append(ino2[index2])
            index2+=1

    if index1<len(ino1):
        mrg_ino.append(ino1[index1])
        index1+=1
    
    elif index2<len(ino2):
        mrg_ino.append(ino2[index2])
        index2+=1

    print(mrg_ino)
    

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

merge(bst1,bst2)