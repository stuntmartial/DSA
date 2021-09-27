def func(arr,low_val,high_val):
    low=0
    mid=0
    high=len(arr)-1

    while mid<high:
        if arr[mid]<low_val:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1

        elif arr[mid]>=low_val and arr[mid]<=high_val:
            mid+=1

        elif arr[mid]>high_val:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1

    print(arr)

arr=[1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
low_val=14
high_val=20
func(arr,low_val,high_val)