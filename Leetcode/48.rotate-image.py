#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reverse(matrix)

    def transpose(self,matrix):
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    def reverse(self,matrix):
        for i in range(len(matrix)):
            p1=0;p2=len(matrix)-1

            while p1<p2:
                matrix[i][p1],matrix[i][p2]=matrix[i][p2],matrix[i][p1]
                p1+=1;p2-=1

            
# @lc code=end

