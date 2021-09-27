def find_peak_ele(arr,beg,end):

	if end >= beg:

		mid = (beg+end) // 2

		if mid == 0:
			if arr[mid] > arr[mid+1]:
				return mid
			else:
				return mid+1

		elif mid == len(arr)-1:
			if arr[mid] > arr[mid-1]:
				return mid
			else:
				return mid-1

		elif arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
			return mid

		elif mid>0 and arr[mid-1]>arr[mid]:
			return find_peak_ele(arr,beg,mid-1)

		else:
			return find_peak_ele(arr,mid+1,end)

print("Enter arr : ")
arr = [int(i) for i in input().split()]
if len(arr) == 1:
	print(arr[0])
else:
	ans = find_peak_ele(arr,0,len(arr)-1)
	print(ans)