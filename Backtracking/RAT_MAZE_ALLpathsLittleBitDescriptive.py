#User function Template for python3
ans=''
class Solution:
    def findPath(self, m, n):
        global ans
        ans = ''
        soln=''
        func(m,n,0,0,soln)
        ans = [i for i in ans.split(' ')]
        ans_=[]
        for i in ans:
            if i==' ':
                continue
            else:
                ans_.append(i)
        print(ans)
        return ans
        
def func(maze,n,x,y,soln):
    global ans
    print(x,y)
    if (x,y) == (n-1,n-1) and isSafe(maze,x,y):
        print(soln)
        for i in soln:
            ans = ans + i
        ans = ans + ' '
        return
    
    maze[x][y] = 0
    soln=soln+'D'
    if isSafe(maze,x+1,y):
        func(maze,n,x+1,y,soln)
    soln=soln[0:len(soln)-1]
    
    soln=soln+'L'
    if isSafe(maze,x,y-1):
        func(maze,n,x,y-1,soln)
    soln=soln[0:len(soln)-1]
    
    soln=soln+'R'
    if isSafe(maze,x,y+1):
        func(maze,n,x,y+1,soln)
    soln=soln[0:len(soln)-1]
    
    soln=soln+'U'
    if isSafe(maze,x-1,y):
        func(maze,n,x-1,y,soln)
    soln=soln[0:len(soln)-1]
    
    maze[x][y]=1
    
def isSafe(maze,x,y):
    if x<0 or y<0 or x>=len(maze) or y>=len(maze):
        return False
    
    if maze[x][y]==0:
        return False
    elif maze[x][y]==1:
        return True
        
arr=[[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
arr2=[[1 ,0, 1, 0],[ 0, 0, 1, 1,],[ 0, 1, 0, 1],[ 0, 0, 1, 1]]
s = Solution()
print(s.findPath(arr2,4))
print(s.findPath(arr,4))