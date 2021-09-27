#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0 or len(height)==1 or len(height)==2:
            return 0        

        waterAbove=self.getWaterAbove(height)
        return sum(waterAbove)
    
    def getWaterAbove(self,heights):
        leftArr=self.getLeftArr(heights)
        rightArr=self.getRightArr(heights)
        waterAbove=list()

        for i in range(len(heights)-1):
            waterAbove_i=0 if leftArr[i]==float("inf") or rightArr[i]==float("inf") else min(leftArr[i], rightArr[i]) - heights[i]
            waterAbove.append(waterAbove_i)
    
        return waterAbove

    def getLeftArr(self,heights):
        stk=list();leftArr=list()

        stk.append(heights[0]);leftArr.append(float("inf"))

        for i in range(1,len(heights)):
            if stk[-1]<heights[i]:
                leftArr.append(float("inf"))
                stk.append(heights[i])
            else:
                leftArr.append(stk[-1])

        return leftArr

    def getRightArr(self,heights):
        stk=list();rightArr=list()
        stk.append(heights[-1]);rightArr.append(float("inf"))

        for i in range(len(heights)-2,-1,-1):
            if stk[-1]<heights[i]:
                rightArr.insert(0,float("inf"))
                stk.append(heights[i])
            else:
                rightArr.insert(0,stk[-1])

        return rightArr

# @lc code=end

