def find_max(arr,beg,end):

	if end>=beg:

		mid = (beg+end)//2

		if mid == 0:
			if arr[mid]>arr[mid+1]:
				return mid
			else:
				return mid+1

		elif mid == len(arr)-1:
			if arr[mid]>arr[mid-1]:
				return mid				
			else:
				return mid-1

		elif arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
			return mid

		elif mid > 0 and arr[mid] > arr[mid-1]:
			return find_max(arr,mid+1,end)

		else:
			return find_max(arr,beg,mid-1)

def binary_search(arr,beg,end,ele):

	if end>=beg:

		mid = (beg+end)//2

		if arr[mid] == ele:
			return mid

		elif arr[mid] < ele:
			return binary_search(arr,mid+1,end,ele)
		else:
			return binary_search(arr,beg,mid-1,ele)

	return -1

def rev_binary_search(arr,beg,end,ele):

	if end>=beg:

		mid = (beg+end)//2

		if arr[mid] == ele:
			return mid

		elif arr[mid] < ele:
			return rev_binary_search(arr,beg,end-1,ele)
		else:
			return rev_binary_search(arr,mid+1,end,ele)

	return -1

print("Enter array : ")
arr = [int(i) for i in input().split()]
ele = int(input("Enter element : "))

if len(arr) == 1: 
	if arr[0] == ele:
		print(0)
		exit()
	else:
		print(-1)
		exit()

index = find_max(arr,0,len(arr)-1)

if arr[index] == ele:
	print(index)

else:

	flag1 = binary_search(arr[0:index-1],0,index-1,ele)
	flag2 = rev_binary_search(arr,index+1,len(arr)-1,ele)

	if flag1 != -1 :
		print(flag1)
	elif flag2 != -1:
		print(flag2)
	else:
		print(-1)