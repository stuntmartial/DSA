class Node:
    def __init__(self,val,left=None,right=None,nxt=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def specif_LOT(self):
        if self.root==None:
            return

        op=[self.root.val]
        q=[root.left,root.right]
        
        while len(q)>0:
            for i in q:
                print(i.val,end='  ')
            print()
            node1=q.pop(0)
            node2=q.pop(0)

            print('node1 : ',node1.val,' node2 : ',node2.val)

            op.append(node1.val)
            op.append(node2.val)

            if node1.left!=None:
                q.append(node1.left)
                q.append(node2.right)
                q.append(node1.right)
                q.append(node2.left)


        print(op)

root = Node(1) 
  
root.left = Node(2) 
root.right = Node(3)  
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.left.left.left = Node(8) 
root.left.left.right = Node(9) 
root.left.right.left = Node(10) 
root.left.right.right = Node(11) 
root.right.left.left = Node(12) 
root.right.left.right = Node(13) 
root.right.right.left = Node(14) 
root.right.right.right = Node(15) 
root.left.left.left.left = Node(16) 
root.left.left.left.right = Node(17) 
root.left.left.right.left = Node(18) 
root.left.left.right.right = Node(19) 
root.left.right.left.left = Node(20) 
root.left.right.left.right = Node(21) 
root.left.right.right.left = Node(22) 
root.left.right.right.right = Node(23) 
root.right.left.left.left = Node(24) 
root.right.left.left.right = Node(25) 
root.right.left.right.left = Node(26) 
root.right.left.right.right = Node(27) 
root.right.right.left.left = Node(28) 
root.right.right.left.right = Node(29) 
root.right.right.right.left = Node(30) 
root.right.right.right.right = Node(31) 

t=Tree(root)
t.specif_LOT()