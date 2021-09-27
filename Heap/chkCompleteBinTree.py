# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root): #root TreeNode) -> bool
        
        #if we encounter any none before discovering a node 
        #that means its not a complete binary tree and hence not a heap
        # IF maxHeap is asked just before pushing node.left and node.right
        #check whether node.val > node.left.val and node.right.val

        if root==None:
            return True
        
        noneFlag = False
        q = [root]
        
        while len(q)>0:
            node = q.pop(0)
            if node.left==None:
                noneFlag=True
            else:
                if noneFlag:
                    return False
                else:
                    q.append(node.left)
            
            if node.right==None:
                noneFlag=True
            else:
                if noneFlag:
                    return False
                else:
                    q.append(node.right)
        
        return True