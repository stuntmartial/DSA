#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1==None and l2==None:
            return ListNode(None)
        
        ptr1=l1;ptr2=l2;prevCarry=0
        opList=LL()
        while ptr1!=None or ptr2!=None:
            if ptr1==None:
                n1=None;n2=ptr2
            elif ptr2==None:
                n1=ptr1;n2=None
            else:
                n1=ptr1;n2=ptr2

            currSum,currCarry=self.customAdd(n1, n2 ,prevCarry)
            opList.ins(currSum)
            prevCarry=currCarry
            if ptr1:
                ptr1=ptr1.next
            if ptr2:
                ptr2=ptr2.next

        if prevCarry!=0:
            opList.ins(prevCarry)

        return opList.retHead()

    def customAdd(self,n1,n2,carry=0):
        if n1==None and n2==None:
            return carry,0
        elif n1==None:
            num1=0;num2=n2.val
        elif n2==None:
            num1=n1.val;num2=0
        else:
            num1=n1.val;num2=n2.val

        currSum=(num1+num2+carry)%10;currCarry=(num1+num2+carry)//10
        return currSum,currCarry

class LL:
    def __init__(self,head=None,tail=None):
        self.head=head;self.tail=tail

    def ins(self,val):
        node=ListNode(val=val)
        if self.head==None:
            self.head=node;self.tail=node;return

        self.tail.next=node;self.tail=node

    def retHead(self):
        return self.head

        

        
# @lc code=end

