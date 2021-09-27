def func(arr):
    min_=arr[0]
    profit=0

    for i in range(1,len(arr)):
        if arr[i]<min_:
            min_=arr[i]

        profit=max(profit,arr[i]-min_)

    print(profit)

arr=[7,3,5,6,1,4,7]
func(arr)