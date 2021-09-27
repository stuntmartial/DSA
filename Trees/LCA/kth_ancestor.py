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

    def dfs(self,node_val,k):
        if self.root==None:
            print('No nodes')
            return
            
        list_of_ancs=[]
        count=[-1]
        self.dfs_helper(self.root,node_val,list_of_ancs,k)
        if len(list_of_ancs)==k:
            print(list_of_ancs)
        else:
            print('node inputted has not ',k,' ancestors')

    def dfs_helper(self,node,node_val,list_of_ancs,k):
        print(node.val)
        if node==None:
            return 0

        elif node.val==node_val:    
            print(list_of_ancs)           
            return 1

        flag1=0;flag2=0
        if node.left!=None:
            flag1=self.dfs_helper(node.left,node_val,list_of_ancs,k)
            if flag1==1:
                if len(list_of_ancs)<k:
                    list_of_ancs.append(node.val)
            
        if node.right!=None:
            flag2=self.dfs_helper(node.right,node_val,list_of_ancs,k)
            if flag2==1:
                if len(list_of_ancs)<k:
                    list_of_ancs.append(node.val)
            
        return flag1 or flag2

arr=[0,1,2,3,4,None,5,None,None,6,None,None,None,7,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
t=Tree(arr)
t.dfs(7,2)