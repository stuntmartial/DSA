def Sub_Set_Sum_rec(arr , n ,sum_ ):

	if sum_ == 0:
		return True
	elif n == 0:
		return False

	if arr[n-1] <= sum_:

		return Sub_Set_Sum_rec(arr , n-1 , sum_ - arr[n-1]) or Sub_Set_Sum_rec(arr,n-1,sum_)

	else :

		return Sub_Set_Sum_rec(arr , n-1 , sum_)

arr = [2,3,7,8,10]
sum_ = 8
print(Sub_Set_Sum_rec(arr,len(arr),sum_))