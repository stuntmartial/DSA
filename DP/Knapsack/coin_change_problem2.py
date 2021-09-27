c = [int(i) for i in input().split()]
T = int(input())
infinity = T + 1000

n = len(c)
dp_arr = list()

for i in range(0,n+1):
	dp_arr.append([-1] * (T+1))

for i in range(0,n+1):
	for j in range(0,T+1):

		if i == 0:
			dp_arr[i][j] = infinity
		elif j == 0:
			dp_arr[i][j] = 0

for j in range(1,T+1):
	if j%c[0] == 0:
		dp_arr[1][j] = int(j/c[0])
	else:
		dp_arr[1][j] = infinity
'''
for i in range(0,n+1):
	for j in range(0,T+1):
		print(dp_arr[i][j],end = "\t")
	print()
'''

for i in range(2,n+1):
	for j in range(1,T+1):
		
		if c[i-1] <= j:
			dp_arr[i][j] = min(1 + dp_arr[i][j-c[i-1]] , dp_arr[i-1][j] )
		else:
			dp_arr[i][j] = dp_arr[i-1][j]	


for i in range(0,n+1):
	for j in range(0,T+1):
		print(dp_arr[i][j],end = "\t")
	print()

