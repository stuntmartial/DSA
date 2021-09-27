class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root

    def preorder(self):
        if self.root==None:
            return

        self.preorder_util(self.root)
    
    def preorder_util(self,node):
        if node==None:
            return

        print(node.val,end='\t')
        self.preorder_util(node.left)
        self.preorder_util(node.right)
        
    def delete(self,key):
        if self.root==None:
            return

        self.delete_util(self.root,key)
        self.preorder()

    def delete_util(self,node,key):
        if node==None:
            return None

        print(node.val)

        if node.val==key:
            if node.left==None and node.right==None:
                node=None
                return node
            elif node.left!=None and node.right!=None:
                newnode=self.find_rightmost(node.left)
                node.val=newnode.val
                root.left=self.delete_util(newnode,newnode.val)
                return None
            else:
                if node.left!=None:
                    return node.left
                elif node.right!=None:
                    return node.right
                return

        if key>node.val:
            node.right=self.delete_util(node.right,key)
        elif key<node.val:
            node.left=self.delete_util(node.left,key)
        return node

root=Node(50)
root.left=Node(40)
root.left.right=Node(45)
root.left.right.left=Node(43)
root.right=Node(60)
root.right.left=Node(55)
root.right.left.right=Node(57)
root.right.right=Node(66)
t=BST(root)
t.delete(43)
