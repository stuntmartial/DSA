class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def chk_Perfect(self):
        if self.root==None:
            return

        level_dict={}
        parent_level=-1
        self.func(self.root,level_dict,parent_level)
        print(level_dict)
        for i in level_dict.keys():
            if len(level_dict[i]) != 2**i:
                print('No')
                return
        
        print('Yes')

    def func(self,node,level_dict,par_lev):
        if node==None:
            return

        try:
            level_dict[par_lev+1].append(node.val)
        except:
            level_dict[par_lev+1]=[node.val]

        self.func(node.left,level_dict,par_lev+1)
        self.func(node.right,level_dict,par_lev+1)

root = Node(10)  
root.left = Node(20)  
root.right = Node(30)    
root.left.left = Node(40)  
root.left.right = Node(50)  
root.right.left = Node(60)  
root.right.right = Node(70)
root.left.right.left =Node(100)
t=Tree(root)
t.chk_Perfect()