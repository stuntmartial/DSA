def median_2_elements(ele1,ele2):
	return (ele1+ele2)/2

def median_3_elements(ele1,ele2,ele3):
	max_=max(ele1,ele2,ele3)
	min_=min(ele1,ele2,ele3)

	if ele1!=max_ and ele1!=min_:
		med_ =ele1

	elif ele2!=max_ and ele2!=min_:
		med_ =ele2

	elif ele3!=max_ and ele3!=min_:
		med_ =ele3

	return med_
	
def median_4_elements(ele1,ele2,ele3,ele4):
	print(ele1,ele2,ele3,ele4)
	max_=max(ele1,ele2,ele3,ele4)
	min_=min(ele1,ele2,ele3,ele4)

	med_=0
	if ele1!=max_ and ele1!=min_:
		med_ +=ele1

	if ele2!=max_ and ele2!=min_:
		med_ +=ele2

	if ele3!=max_ and ele3!=min_:
		med_ +=ele3

	if ele4!=max_ and ele4!=min_:
		med_ +=ele4

	return med_ /2

def median_single_array(arr):
	size=len(arr)

	if size%2==0:
		return (arr[(size-1)//2]+arr[((size-1)//2) +1])/2
	else:
		return arr[(size-1)//2]

def median(arr1,arr2):
	print('arr1-->',arr1,'arr2-->',arr2)
	size1=len(arr1)
	size2=len(arr2)

	if size1==0:
		return median_single_array(arr2)

	elif size1==1:
		if size2==1:
			return median_2_elements(arr1[0],arr2[0])
		
		elif size2%2!=0:
			mid_= (size2-1) // 2
			return median_2_elements(arr2[mid_] , median_3_elements(arr2[mid_-1],arr2[mid_+1],arr1[0]))

		elif size2%2==0:
			mid_= (size2-1) // 2
			return median_3_elements(arr2[mid_],arr2[mid_+1],arr1[0])

	elif size1==2:
		if size2==2:
			return median_4_elements(arr1[0],arr1[1],arr2[0],arr2[1])

		elif size2%2!=0:
			mid_= (size2-1) // 2
			return median_3_elements(	max(arr2[mid_-1],arr1[0]) , arr2[mid_] , min(arr2[mid_+1],arr1[1]) )

		elif size2%2==0:
			mid_= (size2-1) // 2
			print(mid_)
			return median_4_elements(	max(arr2[mid_-1],arr1[0]) , arr2[mid_],arr2[mid_+1] , min(arr2[mid_+2],arr1[1]) )

	mid_1= (size1-1)//2
	mid_2= (size2-1)//2

	if arr1[mid_1]<=arr2[mid_2]:
		return median(arr1[mid_1:size1],arr2[0:mid_2+1])

	elif arr1[mid_1]>arr2[mid_2]:
		return median(arr1[0:mid_1+1],arr2[mid_2:size2])

def find_median(arr1,arr2):
	size1=len(arr1)
	size2=len(arr2)
	med_=0
	if size1<=size2:
		med_=median(arr1,arr2)
	else:
		med_=median(arr2,arr1)

	print(arr1,arr2)
	for i in arr2:
		arr1.append(i)
	arr1.sort()
	print(arr1)
	print(med_)

arr1=[10,12,45,67]#####32
arr2=[1,20,30,70,80,90]

find_median(arr1,arr2)