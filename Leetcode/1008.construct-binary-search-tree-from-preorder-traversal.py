#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:return None

        index=[0];lowerLim=float("-inf");upperLim=float("inf")
        root=self.generateBST(index,preorder,lowerLim,upperLim)
        return root

    def generateBST(self,index,preorder,lowerLim,upperLim):
        node=TreeNode(preorder[index[0]])

        index[0]+=1;
        if index[0]==len(preorder):return node
        
        nxtNodeVal=preorder[index[0]]
        if lowerLim<=nxtNodeVal and nxtNodeVal<node.val:
            node.left=self.generateBST(index, preorder, lowerLim, node.val-1)
        
        if index[0]==len(preorder):return node
        nxtNodeVal=preorder[index[0]]
        if node.val<nxtNodeVal and nxtNodeVal<=upperLim:
            node.right=self.generateBST(index, preorder, node.val+1, upperLim)

        return node
                        
# @lc code=end

