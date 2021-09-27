x = input()
y = input()
n = len(x)
m = len(y)

dp_arr = list()
result = 0
max_posi = 0
max_posj = 0

for i in range(0,n+1):
	dp_arr.append([-1] * (m+1))

for i in range(0,n+1):
	for j in range(0,m+1):
		if i == 0 or j == 0:
			dp_arr[i][j] = 0

for i in range(1,n+1):
	for j in range(1,m+1):

		if x[i-1] == y[j-1]:
			dp_arr[i][j] = 1 + dp_arr[i-1][j-1]
			if result > dp_arr[i][j]:
				result = result
			else:
				result = dp_arr[i][j]
				max_posi = i
				max_posj = j
			

		else:
			dp_arr[i][j] = 0

for i in range(0,n+1):
	for j in range(0,m+1):
		print(dp_arr[i][j] , end = "\t")
	print()

print("Length of longest common substring ---> ",result)

i = max_posi ; j = max_posj ; substr = "" 
print(i,j)
while(i > 0 and j > 0):

	substr = x[i-1] + substr
	i -= 1
	j -= 1
	if dp_arr[i][j] == 0:
		break

print("Longest common Substring ---> ",substr)