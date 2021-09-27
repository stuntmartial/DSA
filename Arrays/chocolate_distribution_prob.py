def func(arr,m):
    arr.sort()
    print(arr)
    i=0
    j=i+m-1
    
    min_diff=float('inf')

    if j>=len(arr):
        print('Error')

    while j<len(arr):
        min_=arr[i]
        max_=arr[j]
        diff=max_-min_
        min_diff=min(min_diff,diff)

        i+=1
        j+=1

    print(min_diff)

arr=[7,3,2,4,9,12,56]
m=3
func(arr,m)