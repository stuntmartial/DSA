w = [1,2,3,4,24]
p = [10,20,30,40,6]
W = 32

t = list()
for i in range(0,len(w)+1):
	t.append([-1] * (W+1))

for i in range(0,len(w)+1):
	for j in range(0,W+1):
		if i==0 or j==0:
			t[i][j] = 0

for i in range(1,len(w)+1):
	for j in range(1,W+1):

		if w[i-1] <= j:
			t[i][j] = max( p[i-1] + t[i-1][j - w[i-1]] , t[i-1][j] )

		elif w[i-1] > j:
			t[i][j] = t[i-1][j]

for i in range(0,len(w)+1):
	for j in range(0,W+1):
		print(t[i][j],end = '\t')

	print()


w0 = W
n = len(w)
res = t[n][w0]
print("res --- >" ,res)

selected_weights = list()

for i in range(n,0,-1):
	if res <= 0:
		break

	elif res == t[i-1][w0]:
		continue

	else:
		selected_weights.append(w[i-1])
		res -= p[i-1]
		w0 -= w[i-1]

print(selected_weights) 