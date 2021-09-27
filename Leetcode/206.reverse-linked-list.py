#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return
        
        return self.reverse(head, None)

    def reverse(self,node,prev):
        if node.next==None:
            node.next=prev
            return node

        nxtBkp=node.next
        node.next=prev
        return self.reverse(nxtBkp, node)

               
# @lc code=end

