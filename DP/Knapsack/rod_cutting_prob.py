l = [1,2,4,5]
p = [2,8,1,4]
length_of_rod = 7

n = len(l)

dp_arr = list()
for i in range(0,n+1):	
	dp_arr.append([-1] * (length_of_rod + 1))

for i in range(0,n+1):
	for j in range(0,length_of_rod + 1):
		if i == 0 or j == 0:
			dp_arr[i][j] = 0
'''
for i in range(0,n+1):
	for j in range(0,length_of_rod + 1):
		print(dp_arr[i][j],end = "\t")

	print()
'''

for i in range(1,n+1):
	for j in range(1,length_of_rod+1):

		if l[i-1] <= j:
			dp_arr[i][j] = max( p[i-1] + dp_arr[i][j-l[i-1]] , dp_arr[i-1][j] )
		else:
			dp_arr[i][j] = dp_arr[i-1][j] 

for i in range(0,n+1):
	for j in range(0,length_of_rod + 1):
		print(dp_arr[i][j],end = "\t")

	print()
