#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None

        return self.deleteNodeUtil(root,key)

    def deleteNodeUtil(self,node,key):
        
        if node==None:
            return
        
        if node.val<key:
            node.right=self.deleteNodeUtil(node.right, key)
        elif node.val>key:
            node.left=self.deleteNodeUtil(node.left, key)
        elif node.val==key:
            if node.left==None and node.right==None:
                node=None;return None
            elif node.left==None and node.right!=None:
                nodeBkp=node.right;node=None;return nodeBkp
            elif node.right==None and node.left!=None:
                nodeBkp=node.left;node=None;return nodeBkp
            else:
                minRight=self.getMin(node.right)
                node.val=minRight.val
                node.right=self.deleteNodeUtil(node.right, minRight.val)
        return node

    def getMin(self,node):
        if node.left==None:
            return node
        return self.getMin(node.left)

# @lc code=end

