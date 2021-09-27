class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,arr):
        if arr[0]==None:
            print('Root cannot be none')
            return

        nodes_arr=[]
        for i in range(len(arr)):
            if arr[i]!=None:
                node=Node(arr[i])
                nodes_arr.append(node)
                if i==0:
                    self.root=node
            else:
                nodes_arr.append(None)

        for i in range(len(arr)):
            if arr[i]!=None:
                left=nodes_arr[2*i+1]
                right=nodes_arr[2*i+2]
                nodes_arr[i].left=left
                nodes_arr[i].right=right

    def anc_des(self,anc,des):
        if self.root==None:
            print('No nodes')
            return

        anc=self.dfs_helper(self.root,anc)
        if anc==None:
            print(anc," is not present")
            return

        des=self.dfs_helper(anc,des)
        if des==None:
            print(des," is not present or NO")
        else:
            print('YES')

    def dfs_helper(self,node,key):
        if node==None or node.val==key:
            return node

        left=self.dfs_helper(node.left,key)
        right=self.dfs_helper(node.right,key)

        if left==None and right==None:
            return None
        elif left==None:
            return right
        elif right==None:
            return left

arr=[0,1,2,3,4,None,5,None,None,6,None,None,None,7,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
t=Tree(arr)
t.anc_des(1,6)