#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRowStat=False
        firstColStat=False

        for i in range(len(matrix[0])):
            if matrix[0][i]==0:
                firstRowStat=True
                break

        for i in range(len(matrix)):
            if matrix[i][0]==0:
                firstColStat=True
                break

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0;matrix[0][j]=0

        #First Row Check
        for col in range(1,len(matrix[0])):
            if matrix[0][col]==0:
                for row in range(1,len(matrix)):
                    matrix[row][col]=0

        #First Col Check
        for row in range(1,len(matrix)):
            if matrix[row][0]==0:
                for col in range(1,len(matrix[0])):
                    matrix[row][col]=0

        if firstRowStat:
            for col in range(len(matrix[0])):
                matrix[0][col]=0

        if firstColStat:
            for row in range(len(matrix)):
                matrix[row][0]=0

def disp(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()
        
# @lc code=end

