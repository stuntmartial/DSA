class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root

    def get_max_min(self):
        if self.root==None:
            return 

        ptr1=self.root
        ptr2=self.root
        while ptr1.right!=None:
            ptr1=ptr1.right
        while ptr2.left!=None:
            ptr2=ptr2.left

        max_=ptr1.val
        min_=ptr2.val
        print(max_,min_)

root=Node(30)
root.left=Node(17)
root.left.left=Node(15)
root.left.left.right=Node(16)
root.left.right=Node(20)
root.right=Node(40)
t=BST(root)
t.get_max_min()