res = -1
def func(arr,beg,end,ele):

	global res

	if end >= beg:
	
		mid = (beg+end) // 2

		if arr[mid] == ele:

			return ele

		elif  arr[mid] < ele:

			res = max(res,arr[mid])
			return func(arr,mid+1,end,ele)

		else:
			return func(arr,beg,mid-1,ele)

	return -1


print("Enter array  : ")
arr = [int(i) for i in input().split()]

ele = int(input("Enter element : "))

flag = func(arr,0,len(arr)-1,ele)

if flag == -1:
	print(res)
else:
	print(flag)