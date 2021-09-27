arr = [int(i) for i in input().split()]

def MCM(arr,i,j):

	if i >= j:
		return 0

	min_op = max(arr) + 100

	for k in range(i,j):

		temp_ans = MCM(arr,i,k) + MCM(arr,k+1,j) + (arr[i-1] * arr[k] * arr[j])

		if temp_ans <= min_op:
			min_op = temp_ans

	print(min_op)
	return min_op

print(MCM(arr,1,(len(arr)-1)))