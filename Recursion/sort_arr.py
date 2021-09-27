def myinsert(arr,ele):

	print("My insert ",arr,ele)

	if len(arr) == 0 or arr[len(arr)-1] <= ele:
		arr.append(ele)
		print(arr)
		

	else:
		temp = arr[len(arr)-1]
		arr.pop(len(arr)-1)
		myinsert(arr,ele)
		arr.append(temp)


def mysort(arr,n):

	print("My sort " , arr,n)
	if len(arr) == 1:
		print("Length 1")
		return 

	temp = arr[len(arr)-1]
	arr.pop(len(arr)-1)
	mysort(arr,n-1)
	print("Before inserting--->",arr)
	myinsert(arr,temp)
	print("After inserting --- >",arr)

print("Enter array ---> ")
arr = [int(i) for i in input().split()]

mysort(arr,len(arr))

print("Sorted array --> ",arr)
