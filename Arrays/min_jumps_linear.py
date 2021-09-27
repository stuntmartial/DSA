def func(arr):
    if arr[0]==0:
        return float('inf')

    ladder=arr[0]
    usable_stairs=arr[0]
    jumps=1
    n=len(arr)

    for i in range(1,n):
        if i+arr[i]>ladder:
            ladder=i+arr[i]
        
        usable_stairs-=1
        if usable_stairs==0:
            jumps+=1
            usable_stairs=ladder-i


    print(jumps)
    return jumps

arr=[1,1,6,1,0,9]
print(arr)
func(arr)