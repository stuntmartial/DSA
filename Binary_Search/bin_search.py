def bin_srch(arr,beg,end,ele):

	if end >= beg :
		mid = ( beg + end ) // 2

		if arr[mid] == ele:
			return mid

		elif ele > arr[mid]:

			pos = bin_srch(arr,mid+1,end,ele)
			return pos

		else:

			pos = bin_srch(arr,beg,mid-1,ele)
			return pos

	return -1

print("Enter array")
arr = [int(i) for i in input().split()]
ele = int(input("Enter element : "))

pos = bin_srch(arr,0,len(arr)-1,ele)

print("Element found at pos :" , pos)