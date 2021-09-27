(n,k) = int(input()),int(input())

def nk(n,k):

	if n==1 or k==1:
		return 0

	mid = (2 ** (n-1))/2

	if k <= mid:
		return nk(n-1,k)
	else:
		return not(nk(n-1,k-mid))

print(int(nk(n,k)))