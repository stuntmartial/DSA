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

def create_tree(arr):
    ht={}
    root=None
    for i in range(len(arr)):
        child=i
        parent=arr[i]
        if parent==-1:
            try:
                print(ht[child])
                root=ht[child]
            except:
                node=Node(child)
                ht[child]=node
                root=node

            continue

        try:
            print(ht[parent])
        except:
            node=Node(parent)
            ht[parent]=node

        try:
            print(ht[child])
        except:
            node=Node(child)
            ht[child]=node

        parent_node=ht[parent]
        child_node=ht[child]

        if parent_node.left==None:
            parent_node.left=child_node
        elif parent_node.right==None:
            parent_node.right=child_node
        else:
            print('error')
            exit()    

    print(root.val)
    t=Tree(root)
    t.inorder()

arr=[1, 5, 5, 2, 2, -1, 3]
create_tree(arr)

