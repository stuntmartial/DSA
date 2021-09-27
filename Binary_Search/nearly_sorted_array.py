def func(arr,beg,end,ele) :

	if end>=beg:

		mid = (beg + end) // 2

		if arr[mid] == ele:
			return mid

		elif (mid-1) >= beg and arr[mid-1] == ele:
			return (mid-1)

		elif (mid+1) <= end and arr[mid+1] == ele:
			return (mid+1)

		elif ele > arr[mid] :
			return func(arr,mid+2,end,ele)

		else:
			return func(arr,beg,mid-2,ele)

	return -1

	
print("Enter array  : ")
arr = [int(i) for i in input().split()]

ele = int(input("Enter element : "))

res = func(arr,0,len(arr)-1,ele)

print(res)


