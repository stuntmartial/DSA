#User function Template for python3
dp = list()
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        global dp
        dp = []
        for i in range(n+1):
            dp.append([-1]*(m+1))
        
        self.func(S1,S2,n,m)
        max_=float('-inf')
        for i in range(n+1):
            for j in range(m+1):
                max_ = max(max_,dp[i][j])

        for i in range(m+1):
            if i==0:
                print('\tNull',end='\t')
                continue
            print(S2[0:i],end='\t')
        print()
        for i in range(n+1):
            if i==0:
                print('Null',end='\t')
            else:
                print(S1[0:i],end='\t')
            for j in range(m+1):
                print(dp[i][j],end='\t')
            print()
                  
        return max_
    
    def func(self,S1,S2,n,m):
        print('Called on n:',n,' m:',m)
        global dp
        
        if n==0 or m==0:
            dp[n][m] = 0
            return 0
        
        if dp[n][m]!=-1:
            return dp[n][m]

        if dp[n-1][m-1]==-1:
            self.func(S1,S2,n-1,m-1)
        if dp[n-1][m]==-1:
            self.func(S1,S2,n-1,m)
        if dp[n][m-1]==-1:
            self.func(S1,S2,n,m-1)
            
            
        if S1[n-1]==S2[m-1]:
            dp[n][m] = 1+dp[n-1][m-1]
            return dp[n][m]
        
        else:
            dp[n][m]=0
            return dp[n][m]
        
sol = Solution()
S1="ABCDGH"
S2="ACDGHR"
sol.longestCommonSubstr(S1,S2,len(S1),len(S2))