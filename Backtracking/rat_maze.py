soln=""
def issafe(arr,ix,iy,n):
    
    if ix<0 or ix>=n or iy<0 or iy>=n or arr[ix][iy]==0 or arr[ix][iy]==2:
        print(ix,iy," is not safe")
        return False
    print(ix,iy,"is safe")
    return True
        

def rec_func(arr,i,j,n):
    global soln

    if i==(n-1) and j==(n-1):
        return True
    
    if issafe(arr,i,j,n):
        arr[i][j]=2

        if rec_func(arr,i+1,j,n)==True:
            soln="D"+soln  
            return True
    
        
        if rec_func(arr,i,j-1,n)==True:
            soln="L"+soln
            return True
        
        if rec_func(arr,i,j+1,n)==True:
            soln="R"+soln
            return True
        
        if rec_func(arr,i-1,j,n)==True:
            soln="U"+soln
            return True
            
        
    return False

def findPath(arr, n):
    global soln
    rec_func(arr,0,0,n)
    if len(soln)==0:
        return -1
    
arr=[[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
findPath(arr,4)