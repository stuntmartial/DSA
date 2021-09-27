pre_index=0
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def inorder(self):
        if self.root==None:
            return
        
        self.func(self.root)
        print()

    def func(self,node):
        if node==None:
            return

        self.func(node.left)
        print(node.val,end='\t')
        self.func(node.right)

def create_tree(pre,post):
    global pre_index
    pre_index=0
    ht={}

    for i in range(0,len(post)):
        ht[post[i]]=i

    print(ht)
    start=0
    end=len(post)-1

    root=utility(pre,post,start,end,ht)
    t=Tree(root)
    t.inorder()

def utility(pre,post,start,end,ht):
    global pre_index
    print(pre_index)
    if start>end or pre_index>=len(post):
        return None
    
    node=Node(pre[pre_index])
    pre_index+=1

    if start==end or pre_index>=len(post):
        return node

    post_index=ht[pre[pre_index]]
    print('post_index--> ',post_index)
    node.left=utility(pre,post,start,post_index,ht)
    node.right=utility(pre,post,post_index+1,end-1,ht)

    return node

pre=[1,2,4,8,9,5,3,6,7]
post=[8,9,4,5,2,6,7,3,1]

create_tree(pre,post)