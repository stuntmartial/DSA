import math
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


        self.ref,self.level_dict=self.preprocessing()

    def get_parent_dict(self):
        if self.root==None:
            print('No nodes')
            return

        parent_dict={self.root.val:None}
        _,level_dict=self.bfs(parent_dict)
        print(parent_dict)
        print()
        print()
        return parent_dict,level_dict

    def bfs(self,parent_dict):
        if self.root==None:
            print('No nodes')
            return
        
        level_dict={self.root.val:0}
        q=[self.root]
        while len(q)>0:
            v=q.pop(0)
            print(v.val)
            if v.left!=None:
                q.append(v.left)
                parent_dict[v.left.val]=v.val
                level_dict[v.left.val]=1+level_dict[v.val]                
            if v.right!=None:
                q.append(v.right)
                parent_dict[v.right.val]=v.val 
                level_dict[v.right.val]=1+level_dict[v.val]
    

        return parent_dict,level_dict

    def preprocessing(self):
        parent_dict,level_dict=self.get_parent_dict()
        n=len(list(parent_dict.keys()))
        no_of_parents=math.ceil((math.log2(n)))
        parent_arr=[]
        for i in range(n):
            parent_arr.append([-1] * no_of_parents)


        for i in range(n):
            for j in range(no_of_parents):
                if j==0 and i!=0:
                    parent_arr[i][j]=parent_dict[i]

        for i in range(1,n):
            for j in range(1,no_of_parents):
                node2=parent_arr[i][j-1]
                parent_arr[i][j]=parent_arr[node2][j-1]

        for i in range(n):
            print(list(parent_dict.keys())[i],end='\t')
            for j in range(no_of_parents):
                print(parent_arr[i][j],end='\t')
            print()

        return parent_arr,level_dict

    def kth_ancs_query(self,node,k):
        if k-1>len(self.ref[0]):
            print(-1)
            return -1        

        #k=k-1
        k=bin(k).replace('0b','')
        print(k)
        node1=node
    
        for i in range(len(k)):
            if k[i]=='0':
                continue
            else:
                jump=(len(k)-1-i)
                node1=self.ref[node1][jump]
                print('jump---> ',jump,'\tnode1---> ',node1)
                if node1==-1:
                    break
        
        return node1

    def lca(self,node1,node2):
        if self.root==None or node1==None or node2==None:
            print('A node is none')
            return 

        print(self.level_dict)

        level1=self.level_dict[node1]
        level2=self.level_dict[node2]
        if level1>level2:
            node1=self.kth_ancs_query(node1,level1-level2)
            level1=level2
        elif level2>level1:
            node2=self.kth_ancs_query(node2,level2-level1)
            level2=level1

        lev=bin(level1).replace('0b','')
        i=0
        print('aaaaaaa---->',lev,node1,node2)
        
        while i<len(lev) and node1!=node2:
            jump=2**(len(lev)-1-i)
            print('JUMPPPP----->',jump)

            if self.kth_ancs_query(node1,jump)!=-1:
                node11=self.kth_ancs_query(node1,jump)
                node22=self.kth_ancs_query(node2,jump)
                print(node11,node22)
                
                if node11==node22:
                    i+=1
                    continue
                else:
                    node1=node11;node2=node22

            i+=1
        if node1==node2:
            print(node1)
        else:
            print(self.ref[node1][0])

arr=[i for i in range(0,15)]
for i in range(16):
    arr.append(None)

print(arr)
t=Tree(arr)
t.lca(5,7)