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

    def lca(self,n1,n2):
        if self.root==None:
            print('No nodes')
            return    
        
        lowest_common_ancestor=self.lca_helper(self.root,n1,n2)
        if lowest_common_ancestor==None:
            print(lowest_common_ancestor)
        else:
            print(lowest_common_ancestor.val)
            return lowest_common_ancestor

    def lca_helper(self,node,n1,n2):
        '''
        the lca_helper assumes both nodes are present
        if we want to detect node not present then 
        chk after entire execution
        at self.root left_stat or right_stat is None
        if any one is that means n1 or n2 node is not present
        '''
        if node==None:
            return node

        if node.val==n1 or node.val==n2:
            return node

        left_stat=self.lca_helper(node.left,n1,n2)
        right_stat=self.lca_helper(node.right,n1,n2)

        if left_stat!=None and right_stat!=None:
            return node
        elif left_stat!=None:
            return left_stat
        elif right_stat!=None:
            return right_stat
        else:
            return None

    def find_dist(self,n1,n2):
        lowest_common_ancestor=self.lca(n1,n2)
        if lowest_common_ancestor==None:
            print('No LCA')
            return

        dist={lowest_common_ancestor.val:0}
        self.dfs_helper(lowest_common_ancestor,dist,n1,n2)
        print('Dist---->',dist[n1]+dist[n2])

    def dfs_helper(self,node,dist,n1,n2):
        if node==None:
            return

        elif node==n1 or node==n2:
            return

        if node.left!=None:
            dist[node.left.val]=dist[node.val]+1
        if node.right!=None:
            dist[node.right.val]=dist[node.val]+1

        self.dfs_helper(node.left,dist,n1,n2)
        self.dfs_helper(node.right,dist,n1,n2)

arr=[1,2,3,4,5,6,7,None,None,None,None,None,None,None,None]
t=Tree(arr)
t.find_dist(4,5)
t.find_dist(4,6)
t.find_dist(3,4)
t.find_dist(2,4)
