print("Enter array :")
arr = [int(i) for i in input().split()]
k = int(input("Enter no of students :"))

if len(arr) < k :
	print("Not possible")
	exit()

beg = max(arr)
end = sum(arr)
res = 10**9

def isvalid(arr,limit,k):

	s = 0;students = 1
	for i in range(0,len(arr)):
		if (s+arr[i]) <= limit:
			s = s+arr[i]
		else:
			s = arr[i]
			students += 1

	return k==students

while end >= beg:

	mid = (beg+end) // 2
	print("beg ---> ",beg,"end -----> ",end,"mid ----> ",mid)

	if isvalid(arr,mid,k):
		res = min(res,mid)
		end = mid - 1

	else:

		beg = mid+1

print(res)