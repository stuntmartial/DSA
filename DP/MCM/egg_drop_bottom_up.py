f = int(input())
e = int(input())

dp_arr = list()

for i in range(0,f+1):
	dp_arr.append([-1] * (e+1))

for i in range(0,f+1):
	for j in range(0,e+1):
		if i==0 or i==1:
			dp_arr[i][j] = i
		elif j==0:
			dp_arr[i][j] = 0
		elif j==1:
			dp_arr[i][j] = i

for i in range(2,f+1):
	for j in range(2,e+1):
		ans = 10000
		for k in range(1,f+1):
			temp_ans = 1 + max(dp_arr[k-1][j-1] , dp_arr[i-k][j])
			ans = min(ans,temp_ans)
		dp_arr[i][j] = ans

print(dp_arr[f][e])



'''
for i in range(0,f+1):
	for j in range(0,e+1):
		print(dp_arr[i][j],end="\t")
	print()
'''