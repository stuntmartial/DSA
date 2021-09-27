def solve(s,k):

	if k == 0:
		s.pop()
		return

	temp = s[len(s) - 1]
	s.pop(len(s) - 1)
	solve(s,k-1)
	s.append(temp)

s = [int(i) for i in input().split()]
k = len(s) // 2
solve(s,k)
print(s)
