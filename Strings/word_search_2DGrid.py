class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        first_char = word[0]
        visited_flag = list()
        for i in range(len(board)):
            visited_flag.append([0]*len(board[0]))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.solve(i,j,board,word,0,visited_flag):
                        return True
                    
        return False
    
    def solve(self,i,j,board,word,index,visited_flag):
        
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return False
        if visited_flag[i][j]==1:
            return False
        
        
        visited_flag[i][j]=1
        
        if index==len(word)-1:
            if board[i][j] == word[index]:
                visited_flag[i][j] = 0
                return True
            else:
                visited_flag[i][j]=0
                return False
            
        op=False
        if board[i][j] == word[index]:
            op1 = self.solve(i+1,j,board,word,index+1,visited_flag)
            op2 = self.solve(i-1,j,board,word,index+1,visited_flag)
            op3 = self.solve(i,j+1,board,word,index+1,visited_flag)
            op4 = self.solve(i,j-1,board,word,index+1,visited_flag)
        
            op = op1 or op2 or op3 or op4
        visited_flag[i][j] = 0
        return op