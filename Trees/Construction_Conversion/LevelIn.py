class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def preorder(self):
        if self.root==None:
            return
        self.func2(self.root)
        print()

    def func2(self,node):
        if node==None:
            return
        print(node.val,end='\t')
        self.func2(node.left)
        self.func2(node.right)

def create_tree(lo,io):
    if len(lo)!=len(io):
        return -1

    start=0
    end=len(lo)-1
    ht={io[i]:i for i in range(0,len(io))}
    print(ht)

    root=func(lo,io,start,end,ht)
    t=Tree(root)
    t.preorder()

def func(lo,io,start,end,ht):
    print(lo,io)
    if start>end:
        return None
    
    node=Node(lo[0])
    if start==end:
        return node

    index=ht[lo[0]]
    print(index)
    ht2={lo[i]:0 for i in range(1,len(lo))}
    
    for i in range(start,index):
        ht2[io[i]]=1
    
    print(ht2)
    left_lo=[]
    for i in range(1,len(lo)):
        if ht2[lo[i]]==1:
            left_lo.append(lo[i])
        
    
    ht2={lo[i]:0 for i in range(1,len(lo))}
    for i in range(index+1,end+1):
        ht2[io[i]]=1

    right_lo=[]
    for i in range(1,len(lo)):
        if ht2[lo[i]]==1:
            right_lo.append(lo[i])

    print('left_lo--->',left_lo)
    print('right_lo-->',right_lo)
    
    node.left=func(left_lo,io,start,index-1,ht)
    node.right=func(right_lo,io,index+1,end,ht)
            
    return node

io=[4, 8, 10, 12, 14, 20, 22]
lo=[20, 8, 22, 4, 12, 10, 14]

create_tree(lo,io)