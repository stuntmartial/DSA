res = 'z'
def func(arr,beg,end,ele):

	global res
	if end >= beg:

		mid = (beg+end) // 2

		if arr[mid] == ele:
			return func(arr,mid+1,end,ele)

		elif arr[mid] > ele:

			res = chr(min(ord(res),ord(arr[mid])))
			return func(arr,beg,mid-1,ele)

		else:

			return func(arr,mid+1,end,ele)

	return -1

print("Enter array  : ")
arr = [i for i in input().split()]

ele = input("Enter element : ")

flag = func(arr,0,len(arr)-1,ele)
print(flag)

if flag == -1:
	print(res)
else:
	print(arr[flag]) 