dp=dict()
level_dict=dict()
level_sum=dict()
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def __init__(self,root):
        self.root=root

    def get_levelSum(self):
        global level_dict,level_sum
        if self.root==None:
            return

        level_dict={self.root:0}
        self.func(self.root)
        return level_sum,max(level_sum.keys())

    def func(self,node):
        global level_dict,level_sum

        if node==None:
            return

        try:
            level_sum[level_dict[node]]+=node.val
        except:
            level_sum[level_dict[node]]=node.val

        if node.left!=None:
            level_dict[node.left]=level_dict[node]+1
            self.func(node.left)
        if node.right!=None:
            level_dict[node.right]=level_dict[node]+1
            self.func(node.right)
        

    def maxS(self):
        global dp
        if self.root==None:
            return

        arr,l=self.get_levelSum()
        print(arr,l)
        if len(arr)==1:
            return arr[0]

        if len(arr)==2:
            return max(arr[0],arr[1])

        dp={}
        s1=self.maxS_helper(arr,0,l)
        s2=self.maxS_helper(arr,1,l)
        print(s1,s2)
        return max(s1,s2)

    def maxS_helper(self,arr,k,l):
        global dp
        print('k----> ',k)
        if (k+2)>l:
            dp[k]=arr[k]
            return arr[k]

        s=0
        for i in range(k+2,l+1):
            if k in dp.keys():
                s1=dp[k]
            else:
                s1=self.maxS_helper(arr,i,l)
            
            print(s1)
            s=max(s,s1)
        
        dp[k]=arr[k]+s
        print('Returning from ',k,'\t',dp[k])
        return dp[k]         
'''
root=Node(10000)
root.left=Node(1)
root.right=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)
root.right.left=Node(5)
root.left.left.left=Node(100)
root.left.left.right=Node(200)
root.right.left.left=Node(300)

t=Tree(root)
t.maxS()
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.left.right = Node(5)
root.right.left.right.left = Node(6)

t=Tree(root)
t.maxS()

print(dp)