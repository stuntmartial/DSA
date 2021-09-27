#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:return None

        currIndex=[0]
        return self.util(root,k,currIndex).val

    def util(self,node,k,currIndex):
        if node==None:return None
        
        left=self.util(node.left,k,currIndex)
        if left:return left
        currIndex[0]+=1
        if currIndex[0]==k:
            return node
        right=self.util(node.right,k,currIndex)
        return right
# @lc code=end

