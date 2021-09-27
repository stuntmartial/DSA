class Node:
    def __init__(self,val,left=None,right=None,nxt=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def func(self):
        
        if self.root==None:
            print('None')
            return
        elif self.root.left==None and self.root.right==None:
            print(node.val)
            return

        q=[self.root]
        count=0
        rtl_flag=False
        op=[]
        while len(q)>0:
            sz=len(q)
            stk=[]
            count+=1
            for i in range(0,sz):
                node=q.pop(0)
                if rtl_flag==False:
                    op.append(node.val)
                elif rtl_flag==True:
                    stk.append(node.val)

                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)

            while len(stk)>0:
                op.append(stk.pop(len(stk)-1))

            if count==2:
                rtl_flag=not(rtl_flag)
                count=0

        print(op)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.left.left.left=Node(8)
root.left.left.right=Node(9)
root.left.right.left=Node(3)
root.left.right.right=Node(1)
root.right.left.left=Node(4)
root.right.left.right=Node(2)
root.right.right.left=Node(7)
root.right.right.right=Node(2)
root.left.left.right.left=Node(16)
root.left.right.right.left=Node(17)
root.left.right.right.right=Node(18)
root.right.left.right.right=Node(19)

t=Tree(root)
t.func()