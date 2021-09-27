MIN=-10000000
MAX=10000000
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

    def find_max_diff(self):
        if self.root==None:
            print('No nodes')
            return

        list_of_nodes=self.dfs()
        max_min_dict={i:[MIN,MAX] for i in list_of_nodes}        
        self.find_max_diff_helper(self.root,max_min_dict)
        print(max_min_dict)
        max_diff_dict={}
        for i in max_min_dict.keys():
            max_diff_dict[i]=max(abs(i-max_min_dict[i][0]),abs(i-max_min_dict[i][1]))
        print(max_diff_dict)

    def find_max_diff_helper(self,node,max_min_dict):

        print('Node--->',node.val)

        if node==None:
            return MIN,MAX

        if node.left==None and node.right==None:
            max_min_dict[node.val]=[node.val,node.val]
            return node.val,node.val

        left_max,left_min=self.find_max_diff_helper(node.left,max_min_dict)
        right_max,right_min=self.find_max_diff_helper(node.right,max_min_dict)

        req_max=max(left_max,right_max)
        req_min=min(left_min,right_min)

        max_min_dict[node.val]=[req_max,req_min]
        return max(req_max,node.val),min(req_min,node.val)
        
    def dfs(self):
        if self.root==None:
            print('No nodes')
            return

        list_of_nodes=[]
        self.dfs_helper(self.root,list_of_nodes)
        print(list_of_nodes)
        return list_of_nodes

    def dfs_helper(self,node,list_of_nodes):
        if node==None:
            return

        list_of_nodes.append(node.val)
        self.dfs_helper(node.left,list_of_nodes)
        self.dfs_helper(node.right,list_of_nodes)

        
arr=[1,2,3,4,5,6,7,None,None,None,None,None,None,None,None]
t=Tree(arr)
t.dfs()
t.find_max_diff()