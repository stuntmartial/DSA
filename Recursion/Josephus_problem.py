res = 0
def func(arr,k,index):

	global res
	if len(arr) == 1:
		res = arr[0]
		return 

	index = (index + k) % len(arr)
	arr.pop(index)

	func(arr,k,index)


print("Enter array : ")
arr = [int(i) for i in input().split()]
#arr1 = [i for i in range(1,41)] ----> 24 will be the ans if k = 7 ,the original params

k = int(input("\n Enter k : ")) - 1

func(arr,k,0)

print("Required no is : " ,res)

