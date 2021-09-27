class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BT:
    def __init__(self,root=None):
        self.root=root

    def create_tree(self,arr):
        if arr[0]==None:
            print('Root cant be None')
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

        for i in range(len(nodes_arr)-1):
            if nodes_arr[i]!=None:
                node=nodes_arr[i]
                left_pos=2*i+1
                right_pos=2*i+2
                
                if left_pos<=len(arr)-1:
                    if nodes_arr[left_pos]!=None:
                        node.left=nodes_arr[left_pos]

                if right_pos<=len(arr)-1:
                    if nodes_arr[right_pos]!=None:
                        node.right=nodes_arr[right_pos]
    
    def level_order(self):
        if self.root==None:
            print('No nodes')
            return 

        q=[self.root]
        oplist=[]
        while len(q)!=0:
            v=q.pop(0)
            print('v--->',v.val)
            oplist.append(v.val)
            if v.left!=None:
                q.append(v.left)
            if v.right!=None:
                q.append(v.right)

        print(oplist)

arr=[1,2,3,4,5,6,None,None,None,None,None,None,None]
bt=BT()
bt.create_tree(arr)
bt.level_order()