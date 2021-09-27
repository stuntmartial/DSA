#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def findDist(root,a,b):
    if root==None or a==None or b==None:
        return -1
        
    lca=get_lca(root,a,b)
    level_dict=get_level_dict(root)
    #print(level_dict)
    lev_lca=level_dict[lca.data]
    lev_a=level_dict[a]
    lev_b=level_dict[b]
    
    dist_a_LCA = lev_a - lev_lca
    dist_b_LCA = lev_b - lev_lca
    dist = dist_a_LCA + dist_b_LCA
    return dist
    
def get_lca(root,node1,node2):
    if root==None or node1==None or node2==None:
        return None
    
    lca = dfs(root,node1,node2)
    return lca

def get_level_dict(root):
    if root==None:
        return {}
        
    level_dict={root.data:1}
    q=[root]
    
    while len(q)>0:
        node=q.pop(0)
        if node.left!=None:
            q.append(node.left)
            level_dict[node.left.data]=level_dict[node.data]+1
        if node.right!=None:
            q.append(node.right)
            level_dict[node.right.data]=level_dict[node.data]+1
            
    return level_dict
    
def dfs(node,node1,node2):
    if node==None or node.data==node1 or node.data==node2:
        return node
    
    lt=dfs(node.left,node1,node2)
    rt=dfs(node.right,node1,node2)
    
    if lt!=None and rt!=None:
        return node
    elif lt!=None:
        return lt
    elif rt!=None:
        return rt
    else:
        return None
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        a, b=map(int, input().split())
        print(findDist(root, a, b))

# } Driver Code Ends