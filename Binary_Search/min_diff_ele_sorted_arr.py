res = -1
pos = -1
def func(arr,beg,end,ele):

	global res
	global pos
	if end >= beg:
		mid = (beg+end) // 2

		if arr[mid] == ele:

			pos = mid
			return arr[mid]

		elif arr[mid] < ele :

			res = max(res,arr[mid])
			pos = mid
			return func(arr,mid+1,end,ele)

		else:

			return func(arr,beg,mid-1,ele)

	else:
		return -1

print("Enter arr : ")
arr = [int(i) for i in input().split()]
ele = int(input("Enter element : "))

flag = func(arr,0,len(arr)-1,ele)
print(flag,res,pos)

if flag != -1:
	print(flag)

else:
	diff1 = abs(ele - res)
	diff2 = abs(ele - arr[pos+1])

	if diff1 < diff2:
		print(res)
	else:
		print(arr[pos+1])