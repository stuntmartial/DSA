def func(arr,beg,end):

	if end >= beg :

		mid = (beg + end) // 2

		if arr[mid-1] > arr[mid] :

			return mid

		elif arr[mid] < arr[end]:
			return func(arr,beg,mid-1)

		else:
			return func(arr,mid+1,end)		

	return -1


print("Enter rotated sorted array : ")

arr = [int(i) for i in input().split()]

res = func(arr,0,len(arr)-1)

print(res)



    