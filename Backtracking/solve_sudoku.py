  n=9
def find_empty_space(arr):
    global n
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                return [i,j]
                
    return -1
    
def remove_val(all_vals,ele):
    if ele not in all_vals:
        return
    for i in range(len(all_vals)):
        if all_vals[i]==ele:
            all_vals.pop(i)
            return
        
def find_sub_grid(index_x,index_y):
    if index_x>=0 and index_x<=2:
        start_x=0
        end_x=2
    elif index_x>=3 and index_x<=5:
        start_x=3
        end_x=5
    elif index_x>=6 and index_x<=8:
        start_x=6
        end_x=8
    
    if index_y>=0 and index_y<=2:
        start_y=0
        end_y=2
    elif index_y>=3 and index_y<=5:
        start_y=3
        end_y=5
    elif index_y>=6 and index_y<=8:
        start_y=6
        end_y=8
        
    return start_x,start_y,end_x,end_y
    
def range_of_vals(arr,index_x,index_y):
    global n
    all_vals=[i for i in range(n+1)]
    
    for i in range(n):
        remove_val(all_vals,arr[index_x][i])
        
    for i in range(n):
        remove_val(all_vals,arr[i][index_y])

    start_x,start_y,end_x,end_y=find_sub_grid(index_x,index_y)
    
    for i in range(start_x,end_x+1):
        for j in range(start_y,end_y+1):
            remove_val(all_vals,arr[i][j])
                       
    return all_vals
    
def disp(arr):
    global n
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()
    
def func(arr):
    l=find_empty_space(arr)
    if l==-1:
        return True
    index_x,index_y=l[0],l[1]
    rov=range_of_vals(arr,index_x,index_y)
    if len(rov)==0:
        return False
    
    for i in rov:
        arr[index_x][index_y]=i
        if func(arr)==True:
            return True
        arr[index_x][index_y]=0

    return False
    
T=int(input())
for i in range(T):
    arr=[]
    for j in range(n):
        l=[int(k) for k in input().split()]
        arr.append(l)
        
    func(arr)
    disp(arr)    