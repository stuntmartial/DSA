#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head==None:return None

        root=self.generateBST(head);return root

    def generateBST(self,head):
        if head==None:return None

        midNode,midNode_prev=self.getMid(head);node=TreeNode(val=midNode.val)
        if midNode_prev:
            midNode_prev.next=None;node.left=self.generateBST(head)
        if midNode.next:
            midNode_next=midNode.next;midNode.next=None;node.right=self.generateBST(midNode_next)

        return node

    def getMid(self,head):
        if head==None:return None,None
        
        prev=None;sptr=head;fptr=head
        while fptr.next!=None and fptr.next.next!=None:
            prev=sptr;sptr=sptr.next;fptr=fptr.next.next

        return sptr,prev

# @lc code=end

