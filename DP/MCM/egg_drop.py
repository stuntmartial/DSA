f = int(input())
e = int(input())

t = list()
for i in range (f+1):
	t.append([-1] * (e+1))

print(t)

def egg_drop(f,e):

	if f == 0 or f == 1:
		return f

	if e == 0:
		return 0

	if e == 1:
		return f

	if t[f][e] != -1:
		return t[f][e]

	ans = 1000

	for k in range(1,f+1):

		if t[k-1][e-1] != -1:
			a = t[k-1][e-1]
		else:
			a = egg_drop(k-1,e-1)

		if t[f-k][e] != -1:
			b = t[f-k][e]
		else:
			b = egg_drop(f-k,e)

		temp_ans = 1 + max(a,b)

		ans = min(ans,temp_ans)

	return ans

print(egg_drop(f,e))
