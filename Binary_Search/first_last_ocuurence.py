def first_pos(arr,beg,end,ele):

	if end >= beg:

		mid = (beg+end) // 2

		if (mid == 0 or arr[mid-1] < ele) and arr[mid] == ele:
			return mid

		elif ele > arr[mid]:

			pos = first_pos(arr,mid+1,end,ele)
			return pos

		elif ele <= arr[mid]:

			pos = first_pos(arr,beg,mid-1,ele)
			return pos

	return -1

def last_pos(arr,beg,end,ele):

	if end >= beg:

		mid = (beg+end) // 2

		if (mid == (len(arr) - 1) or arr[mid+1] > ele) and arr[mid] == ele:
			return mid

		elif ele >= arr[mid]:

			pos = last_pos(arr,mid+1,end,ele)
			return pos

		elif ele < arr[mid]:

			pos = last_pos(arr,beg,mid-1,ele)
			return pos

	return -1
print("Enter array : ")
arr = [int(i) for i in input().split()]
ele = int(input("Enter ele : "))

f = first_pos(arr,0,len(arr)-1,ele)
l = last_pos(arr,0,len(arr)-1,ele)

print(f,l)