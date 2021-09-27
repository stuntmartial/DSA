arr = [1,2,3]

def check_equal_sum(arr):

	s = sum(arr)
	if s % 2 != 0:
		return False
	else:
		return Sub_Set_Sum(arr,s/2)

def Sub_Set_Sum(arr,s):

	n = len(arr)
	s = int(s)
	t = list()
	for i in range(0,n+1):
		t.append( [-1] * (s+1))

	for i in range(0,n+1):
		for j in range(0,s+1):	
			if j == 0:
				t[i][j] = True
			elif i == 0:
				t[i][j] = False

	for i in range(1,n+1):
		for j in range(1,s+1):
			if arr[i-1]<=j:
				t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
			else:
				t[i][j] = t[i-1][j]


	for i in range(0,n+1):
			for j in range(0,s+1):
				print(t[i][j],end = "\t")
			print()

	return t[n][s]

print(check_equal_sum(arr))