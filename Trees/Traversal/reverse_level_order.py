class Node:
    def __init__(self,val,left=None,right=None,nxt=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def rev_order(self):
        if self.root==None:
            return

        q=[self.root]
        stk=[]
        while len(q)>0:
            node=q.pop(0)
            print(node.val)
            stk.append(node.val)
            if node.right!=None:
                q.append(node.right)
            if node.left!=None:
                q.append(node.left)

        op=[]
        while len(stk)>0:
            op.append(stk.pop(len(stk)-1))

        print(op)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

t=Tree(root)
t.rev_order()
