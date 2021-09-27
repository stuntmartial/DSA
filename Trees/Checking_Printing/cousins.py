class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def find_cousins(self,node1,node2):
        if node1==None or node2==None or self.root==None:
            return

        level_dict={self.root.val:0}
        parent1=[None];parent2=[None]
        parent=None
        self.func(self.root,parent,node1,node2,parent1,parent2,level_dict)

        if parent1==None or parent2==None:
            print('No')
            return

        if level_dict[node1]==level_dict[node2] and parent1!=parent2:
            print('Yes')
        else:
            print('No')

    def func(self,node,parent,node1,node2,parent1,parent2,level_dict):
        if node==None:
            return

        if node.left!=None:
            level_dict[node.left.val]=level_dict[node.val]+1
        if node.right!=None:
            level_dict[node.right.val]=level_dict[node.val]+1

        if node.val==node1:
            if parent1[0]!=None:
                parent2[0]=parent
                return
            else:
                parent1[0]=parent
                return

        if node.val==node2:
            if parent1[0]!=None:
                parent2[0]=parent
                return
            else:
                parent1[0]=parent
                return

        self.func(node.left,node,node1,node2,parent1,parent2,level_dict)
        self.func(node.right,node,node1,node2,parent1,parent2,level_dict)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.right.right = Node(15) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8)

t=Tree(root)
t.find_cousins(7,2)