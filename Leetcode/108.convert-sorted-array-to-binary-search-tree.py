#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:return None

        root=self.generateBST(nums);return root

    def generateBST(self,arr):
        if len(arr)==0:return None
        mid=len(arr)//2;node=TreeNode(arr[mid])

        node.left=self.generateBST(arr[0:mid])
        node.right=self.generateBST(arr[mid+1:])

        return node
# @lc code=end

