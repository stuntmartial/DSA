x = input("Enter a string : ")
n = len(x)

t = list()
for i in range(0,n):
	t.append([-1] * (n))

def ispalindrome(x):
	rev = ""
	for i in range(len(x)-1 , -1 , -1):
		rev = rev + x[i]

	return x == rev

def palpat(x,i,j):

	if i >= j or ispalindrome(x[i:j+1]):
		return 0

	if t[i][j] != -1:
		return t[i][j]

	ans = 1000
	for k in range(i,j):

		if t[i][k] != -1:
			left_ans = t[i][k]
		else:
			left_ans = palpat(x,i,k)

		if t[k+1][j] != -1:
			right_ans = t[k+1][j]
		else:
			right_ans = palpat(x,k+1,j)

		temp_ans = 1 + left_ans + right_ans

		ans = min(ans,temp_ans)

	return ans

print(palpat(x,0,len(x)-1))
