x = input()
y = input()
n = len(x)
m = len(y)
global t
t = list()

for i in range(0,n+1):
	t.append([-1] * (m+1))

def lcs(x,y,n,m):

	if n == 0 or m == 0:
		return 0

	if t[n][m] != -1:
		return t[n][m]

	else:
		if x[n-1] == y[m-1]:
			t[n][m] = 1 + lcs(x,y,n-1,m-1)
			return t[n][m]

		else:
			t[n][m] = max( lcs(x,y,n-1,m) , lcs(x,y,n,m-1) )
			return t[n][m]

print(lcs(x,y,n,m))

for i in range(0,n+1):
	for j in range(0,m+1):
		print(t[i][j],end = "\t")
	print()
		