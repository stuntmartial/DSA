x = input("Enter the boolean string :")
global t
n = len(x)

tf = list()
tt = list()

def initialise(t,n):

	for i in range(n):
		t.append([-1] * (n))

initialise(tf,n)
initialise(tt,n)

t = {0:tf , 1:tt}

def bool_par(x,i,j,isTrue):

	if i>j :
		return 0

	if i == j:

		if isTrue == True:
			if x[i] == 'T':
				return 1
			else:
				return 0

		elif isTrue == False:
			if x[i] == 'F':
				return 1
			else:
				return 0

	if t[int(isTrue)][i][j] != -1:
		return t[isTrue][i][j]

	ans = 0
	for k in range (i+1,j,2):

		lt = bool_par(x,i,k-1,True)
		lf = bool_par(x,i,k-1,False)
		rt = bool_par(x,k+1,j,True)
		rf = bool_par(x,k+1,j,False)

		if isTrue == True:
			if x[k] == '&':
				ans += (lt * rt)

			elif x[k] == '|':
				ans += (lt*rt) + (lf*rt) + (lt*rf)

			elif x[k] == '^':
				ans += (lt*rf) + (lf*rt)



		elif isTrue == False:
			if x[k] == '&':
				ans += (lf*rt) + (lt*rf) + (lf*rf)

			elif x[k] == '|':
				ans += (lf*rf)

			elif x[k] == '^':
				ans += (lt*rt) + (lf*rf)

	t[int(isTrue)][i][j] = ans 

	return ans
	
print(bool_par(x,0,len(x)-1,True))	
