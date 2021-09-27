class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root

    def ins(self,key):
        self.ins_util(self.root,key)

    def ins_util(self,node,key):
        if node==None:
            node=Node(key)
            print(node.val)
            return

        print(node.val)
        if key>node.val:
            print('Going right')
            self.ins_util(node.right,key)
        elif key<node.val:
            print('Going left')
            self.ins_util(node.left,key)

root=Node(30)
root.left=Node(17)
root.left.left=Node(15)
root.left.left.right=Node(16)
root.left.right=Node(20)
root.right=Node(40)
t=BST(root)
t.ins(48)