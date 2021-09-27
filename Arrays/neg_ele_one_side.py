def func(arr):
    low=0
    mid=0

    while mid<len(arr):
        if arr[mid]>=0:
            mid+=1

        elif arr[mid]<0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
    print(arr)

arr=[8,-2,-4,7,9,10,-3]
func(arr)