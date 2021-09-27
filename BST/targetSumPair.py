class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root

    def push(self,stack,node,left_flag):
        if node==None:
            return

        #if node is not self.root:
        stack.append(node)
        if left_flag:
            while node.left!=None:
                stack.append(node.left)
                node=node.left
        else:
            while node.right!=None:
                stack.append(node.right)
                node=node.right

    def target_sum(self,target):
        if self.root==None:
            return
        
        c1=c2=self.root
        s1=[self.root]
        s2=[]
        llll=0
        while s1 or s2 or c1 or c2:
            
            '''
            print('s1--->',end='  ')
            for i in s1:
                print(i.val,end='  ')
            print()
            print('s2--->',end='  ')
            for i in s2:
                print(i.val,end='  ')
            print()
            '''

            if c1 or c2:
                if c1:
                    self.push(s1,c1,True)
                    c1=None
                if c2:
                    self.push(s2,c2,False)
                    c2=None
            
            else:
                print('Entering else')
                c1=s1.pop(len(s1)-1)
                c2=s2.pop(len(s2)-1)
                print(c1.val,c2.val)    
                if c1.val>=c2.val:
                    print('No pairs exist')
                    return
                
                s=c1.val+c2.val
                if s==target:
                    print('Pairs exist')
                    return

                elif s>target:
                    self.push(s2,c2.left,False)
                    s1.append(c1)
                    c1=None
                    c2=None
                elif s<target:
                    self.push(s1,c1.right,True)
                    s2.append(c2)
                    c1=None
                    c2=None

            
            
root=Node(70)
root.left=Node(51)
root.left.left=Node(40)
root.left.left.left=Node(30)
root.left.right=Node(60)
root.left.right.left=Node(55)
root.right=Node(82)
root.right.left=Node(75)
root.right.left.right=Node(79)
root.right.right=Node(90)
t=BST(root)
t.target_sum(140)