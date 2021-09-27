def separate(arr):
	print(arr)
	if len(arr)>1:
		
		mid=len(arr)//2
		l=arr[:mid]
		r=arr[mid:]
		separate(l)
		separate(r)

		print("Arrays to be merged ---->",l," ",r)
		print("Full array--->",arr)
		i=0
		j=0
		k=0
		while i<len(l) and j<len(r):
			print(i,j)
		
			if l[i]<=r[j]:
				arr[k]=l[i]
				i+=1
			elif r[j]<=l[i]:
				arr[k]=r[j]
				j+=1
			k+=1

		while  i<len(l):
			arr[k]=l[i]
			i+=1
			k+=1
		while  j<len(r):
			arr[k]=r[j]
			j+=1
			k+=1

arr=[1,5,2,4,3]
separate(arr)
#merge(arr,0,0,1)
print(arr)
			
