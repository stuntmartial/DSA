left_list=[]
right_list=[]
left_boundary=[]
right_boundary=[]
leaves=[]
class Node:
    def __init__(self,val,left=None,right=None,nxt=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root
    
    def boundary_traversal(self):
        global left_list,right_list,left_boundary,right_boundary
        left_list=[]
        right_list=[]
        left_boundary=[]
        right_boundary=[]
        leaves=[]    
        if self.root==None:
            return

        pl=1
        pr=1
        left=1
        right=1
        self.func(self.root,pl,pr,left,right)
        print(left_list,right_list,left_boundary,right_boundary)
        boundary_traversal=[]
        for i in left_boundary:
            boundary_traversal.append(i)
        for i in left_list:
            boundary_traversal.append(i)
        for i in right_list:
            boundary_traversal.append(i)
        for i in right_boundary:
            boundary_traversal.append(i)
        print(boundary_traversal)

    def func(self,node,pl,pr,left,right):
        global left_list,right_list,left_boundary,right_boundary
        
        if node==None:
            return
        if node==self.root:
            left_boundary.append(node.val)
            self.func(node.left,1,0,1,0)
            self.func(node.right,0,1,0,1)
            return
        
        if pl==1 or pr==1:
            if pl==1:
                left_boundary.append(node.val)
                if node.left!=None:
                    self.func(node.left,1,0,left,right)
                    self.func(node.right,0,0,left,right)
                else:
                    self.func(node.right,1,0,left,right)
                return
            if pr==1:
                right_boundary.insert(0,node.val)
                if node.right!=None:
                    self.func(node.left,0,0,left,right)
                    self.func(node.right,0,1,left,right)
                else:
                    self.func(node.left,0,1,left,right)
                return 

        elif node.left==node.right==None:
            if left==1 or right==1:
                if left==1:
                    left_list.append(node.val)
                    return
                if right==1:
                    right_list.append(node.val)
                    return

        self.func(node.left,0,0,left,right)
        self.func(node.right,0,0,left,right)


root=Node(1)
root.left=Node(2)
root.left.right=Node(3)
root.left.right.right=Node(30)
root.left.right.left=Node(4)
root.right=Node(5)
root.right.left=Node(8)
root.right.right=Node(6)
root.right.right.left=Node(7)
root.right.right.left.left=Node(9)

t=Tree(root)
t.boundary_traversal()

root2 = Node(20) 
root2.left = Node(8) 
root2.left.left = Node(4) 
root2.left.right = Node(12) 
root2.left.right.left = Node(100) 
root2.left.right.right = Node(14) 
root2.right = Node(22) 
root2.right.right = Node(25) 
root2.left.right.left.left=Node(10)
root2.right.left=Node(17)
root2.right.left.left=Node(12)
root2.right.left.right=Node(28)

t2=Tree(root2)
t2.boundary_traversal()

root3=Node(20)
root3.left = Node(8)
root3.right = Node(22)
root3.right.right = Node(25)
root3.left.left = Node(4)
root3.left.right = Node(12)
root3.left.right.left = Node(10)
root3.left.right.right = Node(14)
root3.left.right.left.left = Node(10)

t3=Tree(root3)
t3.boundary_traversal()
