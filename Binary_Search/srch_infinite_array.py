def binary_search(arr,beg,end,ele):

	if end >= beg:

		mid = (beg+end) // 2

		if arr[mid] == ele:
			return mid

		elif arr[mid] < ele:
			return binary_search(arr,mid+1,end,ele)

		else:
			return binary_search(arr,beg,mid-1,ele)

	return -1

print("Enter array : ")
arr = [int(i) for i in input().split()]
ele = int(input("Enter element : "))

beg = 0
end = 1

while(ele > arr[end]):

	beg = end
	end *= 2

flag = binary_search(arr,beg,end,ele)

if flag == -1:
	print("Not found")

else:
	print(flag)


# This question should return list index out of range
# cuz end *= 2 without any limit
# Since according to ques an infinite array should be inputted
# But thats not possible
# So theoretically the code is r8
