x = input()
n = len(x)
y = ""
for i in x:
	y = i + y

dp_arr = list()
for i in range(0,n+1):
	dp_arr.append([-1] * (n+1))

for i in range(0,n+1):
	for j in range(0,n+1):
		if i == 0 or j == 0:
			dp_arr[i][j] = 0

for i in range(1,n+1):
	for j in range(1,n+1):

		if x[i-1] == y[j-1]:
			dp_arr[i][j] = 1 + dp_arr[i-1][j-1]
		else:
			dp_arr[i][j] = max(dp_arr[i-1][j] , dp_arr[i][j-1])

for i in range(0,n+1):
	for j in range(0,n+1):
			print(dp_arr[i][j],end = "\t")
	print()

print("Length of LPS ----> ", dp_arr[n][n])

i = n ; j = n
subseqpal = ""

while(i>0 and j>0):

	if x[i-1] == y[j-1]:
		subseqpal = x[i-1] + subseqpal
		i -= 1;j-=1

	elif dp_arr[i-1][j] > dp_arr[i][j-1]:
		i -= 1
	else:
		j -= 1

print("Longest Palindrome Subseq -----> ", subseqpal)