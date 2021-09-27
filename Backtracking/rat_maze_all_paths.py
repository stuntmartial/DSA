oplist=[]

def disp(arr,n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()
    print()

def issafe(arr,ix,iy,n):
    
    if ix<0 or ix>=n or iy<0 or iy>=n or arr[ix][iy]==0 or arr[ix][iy]==2:
        print(ix,iy," is not safe")
        return False
    print(ix,iy,"is safe")
    return True
        

def rec_func(arr,i,j,n,soln,visited_list):
    global oplist
    if i==(n-1) and j==(n-1):
        if issafe(arr,i,j,n):
            oplist.append(soln)
            print("\noplist----->",oplist)
            return 
    
    
    if issafe(arr,i,j,n):
        arr[i][j]=2

        rec_func(arr,i+1,j,n,soln+"D",visited_list+[(i,j)])
        

        rec_func(arr,i,j-1,n,soln+"L",visited_list+[(i,j)])    
        

        rec_func(arr,i,j+1,n,soln+"R",visited_list+[(i,j)])
        

        rec_func(arr,i-1,j,n,soln+"U",visited_list+[(i,j)])
        

        arr[i][j]=1 

    #cell: safe -> so visit : cell_value:1->2
    #move in all possible paths to get to a solution
    #before returning just unvisit the cell cell_value:2->1    


def findPath(arr, n):
    global oplist
    oplist=[]
    rec_func(arr,0,0,n,"",[])
    if len(oplist)==0:
        print(-1)
    else:
        print(oplist)
   
arr=[[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
findPath(arr,4)
arr2=[[1,0],[1,0]]
findPath(arr2,2)

arr3=[[1,0,0,0,0],[1,1,1,1,1],[1,1,1,0,1],[0,0,0,0,1],[0,0,0,0,1]]
disp(arr3,5)
findPath(arr3,5)