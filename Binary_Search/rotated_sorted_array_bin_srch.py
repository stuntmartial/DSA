def bin_srch_rot_arr(arr,beg,end,ele):

	global flag
	mid = (beg + end) // 2

	if arr[mid] == ele:
		flag = 1
		return mid

	elif ele > arr[mid]:

		pos = bin_srch_rot_arr(arr,beg,mid-1,ele)
		return pos

	elif ele < arr[mid]:

		pos = bin_srch_rot_arr(arr,mid+1,end,ele)
		return pos

print("Enter array")
arr = [int(i) for i in input().split()]
ele = int(input("Enter element : "))

flag = 0
pos = bin_srch_rot_arr(arr,0,len(arr)-1,ele)

if flag == 0:
	print("Element not found")

elif flag == 1:
	print("Element found at pos :" , (pos+1))