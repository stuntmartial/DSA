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

        arr=[]
        self.func(self.root,arr)
        return arr

    def func(self,node,arr):
        if node==None:
            return 

        self.func(node.left,arr)
        arr.append(node.val)
        self.func(node.right,arr)

def min_swaps(bt):
    arr=bt.inorder()
    ht={arr[i]:i for i in range(len(arr))}
    print(arr)
    print(ht)
    arr.sort()
    print(arr)
    i=0
    swaps=0
    while i<len(arr):
        if i==ht[arr[i]]:
            i+=1
            continue

        else:
            index=ht[arr[i]]
            arr[i],arr[index]=arr[index],arr[i]
            swaps+=1
            

    print(swaps)

root=Node(5)
root.left=Node(6)
root.right=Node(7)
root.left.left=Node(8)
root.left.right=Node(9)
root.right.left=Node(10)
root.right.right=Node(11)

t=Tree(root)
min_swaps(t)