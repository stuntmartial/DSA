x = input()
y = input()
n = len(x)
m = len(y)

dp_arr = list()
for i in range(0,n+1):
	dp_arr.append([-1] * (m+1))

for i in range(0,n+1):
	for j in range(0,m+1):
		if i==0 or j==0:
			dp_arr[i][j] = 0

for i in range(1,n+1):
	for j in range(1,m+1):

		if x[i-1] == y[j-1]:
			dp_arr[i][j] = 1 + dp_arr[i-1][j-1]
		else:
			dp_arr[i][j] = max(dp_arr[i-1][j] , dp_arr[i][j-1])

for i in range(0,n+1):
	for j in range(0,m+1):
		print(dp_arr[i][j],end = "\t")
	print()

i = n
j = m
scs = ""

while (i>0 and j>0):

	if x[i-1] == y[j-1]:
		scs = x[i-1] + scs
		i -= 1
		j -= 1

	elif dp_arr[i-1][j] >= dp_arr[i][j-1]:
		scs = x[i-1] + scs
		i -= 1
	else:
		scs = y[j-1] + scs
		j -= 1

while i>0:
	scs = x[i-1] + scs
	i -= 1

while j>0:
	scs = y[j-1] + scs
	j -= 1

print(scs)