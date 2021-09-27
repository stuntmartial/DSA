def func(arr):
    i=0
    j=len(arr)-1
    ops=0

    while i<=j:
        if arr[i]==arr[j]:
            i+=1
            j-=1

        elif arr[i]<arr[j]:
            i+=1
            arr[i]+=arr[i-1]
            ops+=1

        elif arr[j]<arr[i]:
            j-=1
            arr[j]+=arr[j+1]
            ops+=1

    print(ops)

arr=[1, 4, 5, 9, 1]
func(arr)