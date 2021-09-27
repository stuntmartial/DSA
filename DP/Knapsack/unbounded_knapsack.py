w = [3,1,2]
p = [10,5,7]
W = 4

dp_arr = list()
for i in range(len(w)+1):
	dp_arr.append([-1] * (W+1))

for i in range(len(w)+1):
	for j in range(W+1):
		if i == 0 or j == 0:
			dp_arr[i][j] = 0

'''
for i in range(len(w)+1):
	for j in range(W+1):
		print(dp_arr[i][j],end = "\t")
	print()
'''

for i in range(1,len(w)+1):
	for j in range(1,W+1):

		if w[i-1] <= j:
			dp_arr[i][j] = max(p[i-1] + dp_arr[i][j- w[i-1]] , dp_arr[i-1][j])

		else:
			dp_arr[i][j] = dp_arr[i-1][j]

for i in range(len(w)+1):
	for j in range(W+1):
		print(dp_arr[i][j],end = "\t")
	print()