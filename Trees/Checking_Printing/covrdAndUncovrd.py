class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def func(self):
        if self.root==None:
            return

        pl=1
        pr=1
        sc=[]
        su=[]
        self.func_helper(root,pl,pr,sc,su)
        print(sc,su)

    def func_helper(self,node,pl,pr,sc,su):
        if node==None:
            return 

        print('Node---> ',node.val,' pl: ',pl,' pr: ',pr)
        if pl==1 or pr==1:
            su.append(node.val)
        else:
            sc.append(node.val)
        
        if pl==1 and pr==1:
            self.func_helper(node.left,1,0,sc,su)
            self.func_helper(node.right,0,1,sc,su)
        
        elif pl==1:
            if node.left!=None:
                self.func_helper(node.left,1,0,sc,su)
                self.func_helper(node.right,0,0,sc,su)
            else:
                self.func_helper(node.right,1,0,sc,su)

        elif pr==1:
            if node.right!=None:
                self.func_helper(node.left,0,0,sc,su)
                self.func_helper(node.right,0,1,sc,su)
            else:
                self.func_helper(node.left,0,1,sc,su)
        elif pl!=1 and pr!=1:
            self.func_helper(node.left,0,0,sc,su)
            self.func_helper(node.right,0,0,sc,su)

        
root = Node(8)  
root.left = Node(3)    
root.left.left = Node(1)      
root.left.right = Node(6)  
root.left.right.left = Node(4)  
root.left.right.right = Node(7)  
root.right = Node(10)  
root.right.right = Node(14)  
root.right.right.left = Node(13)

t=Tree(root)
t.func()