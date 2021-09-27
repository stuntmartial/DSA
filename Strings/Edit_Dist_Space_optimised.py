class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1 = len(word1)
        n2 = len(word2)

        if n1==0:
            return n2
        elif n2==0:
            return n1
        
        dp_arr = []
        for i in range(2):
            dp_arr.append([0]*(n2+1))
            
        for i in range(2):
            for j in range(n2+1):
                if i==0:
                    dp_arr[i][j]=j
                elif j==0:
                    dp_arr[i][j]=i
                    
        print(dp_arr)
                    
        for i in range(1,n1+1):
            dp_arr[1][0] = 1+dp_arr[0][0]
            for j in range(1,n2+1):
                add_ = dp_arr[1][j-1]
                del_ = dp_arr[0][j]
                rep_ = dp_arr[0][j-1]
                if word1[i-1] == word2[j-1]:
                    dp_arr[1][j] = rep_
                else:
                    dp_arr[1][j] = 1+min(add_,del_,rep_)

            print('dp_arr[0]: ',dp_arr[0])
            print('dp_arr[1]: ',dp_arr[1])

            #dp_arr[0][0] = dp_arr[1][0]+1
            for j in range(0,n2+1):
                dp_arr[0][j] = dp_arr[1][j]
            

            print('After overwrite')
            print('dp_arr[0]: ',dp_arr[0])
            print('dp_arr[1]: ',dp_arr[1])
            print()
               
                
        return dp_arr[1][n2]

s=Solution()
word1='dinitrophenylhydrazine'
word2='dimethylhydrazine'
s.minDistance(word1,word2)