class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        
        dp=list()
        for i in range(n1+1):
            dp.append([0]*(n2+1))
            
            
        for i in range(n1+1):
            for j in range(n2+1):
                if i==0:
                    dp[i][j] = j
                elif j==0:
                    dp[i][j] = i
                    
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                add_ = dp[i][j-1] 
                del_ = dp[i-1][j]
                rep_ = dp[i-1][j-1]
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = rep_
                else:
                    dp[i][j] = 1 + min(add_ , del_ , rep_)

        for i in range(n1+1):
            for j in range(n2+1):
                print(dp[i][j],end='\t')
            print()
                
        return dp[n1][n2]

s=Solution()
word1='dinitrophenylhydrazine'
word2='dimethylhydrazine'
s.minDistance(word1,word2)