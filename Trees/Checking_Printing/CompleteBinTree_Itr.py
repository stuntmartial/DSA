class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def chkcom(self):
        q=[self.root]
        flag=0

        while len(q)>0:
            disp(q)
            node=q.pop(0)

            if node.left!=None:
                if flag==1:
                    print('False')
                    return
                else:
                    q.append(node.left)
            else:
                flag=1
            
            if node.right!=None:
                if flag==1:
                    print('False')
                    return
                else:
                    q.append(node.right)
            else:
                flag=1

        print('True')

def disp(q):
    l=[]
    for i in q:
        l.append(i.val)
    print(l)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(6) 

t=Tree(root)
t.chkcom()