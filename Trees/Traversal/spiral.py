class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def spiral_trav(self):
        s1=[self.root]
        s2=[]

        while len(s1)>0 or len(s2)>0:

            while len(s1)>0:
                node=s1.pop(len(s1)-1)
                print(node.val,end='\t')
                if node.right!=None:
                    s2.append(node.right)
                if node.left!=None:
                    s2.append(node.left)

            while len(s2)>0:
                node=s2.pop(len(s2)-1)
                print(node.val,end='\t')
                if node.left!=None:
                    s1.append(node.left)
                if node.right!=None:
                    s1.append(node.right)
                
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

t=Tree(root)
t.spiral_trav()