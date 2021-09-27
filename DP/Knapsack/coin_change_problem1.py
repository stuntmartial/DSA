c = [int(i) for i in input().split()]
T = int(input())

n = len(c)
dp_arr = list()

for i in range(0,n+1):
	dp_arr.append([-1] * (T+1))

'''
for i in range(0,n+1):
	for j in range(0,T+1):
		print(dp_arr[i][j],end = "\t")
	print()
'''

for i in range(0,n+1):
	for j in range(0,T+1):
		if j == 0:
			dp_arr[i][j] = 1
		elif i == 0:
			dp_arr[i][j] = 0

for i in range(1,n+1):
	for j in range(1,T+1):

		if c[i-1] <= j:
			dp_arr[i][j] = dp_arr[i][j-c[i-1]] + dp_arr[i-1][j]
		else:
			dp_arr[i][j] = dp_arr[i-1][j]

for i in range(0,n+1):
	for j in range(0,T+1):
		print(dp_arr[i][j],end = "\t")
	print()

print("Max number of ways ---->",dp_arr[n][T])
