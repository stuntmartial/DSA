def func(arr):
    n=len(arr)

    for i in range(n):
        arr[arr[i]%n] += n

    print(arr)

    for i in range(n):
        arr[i] = int(arr[i]/n)

    print(arr)

arr=[5,5,6,1,2,3,4,5,4]
func(arr)