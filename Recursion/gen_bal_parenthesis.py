def func(n,co,cc,curr,pos):

	if cc == n:
		
		'''
		for i in curr:
			print(i,end = "")
		print()
		'''
		l.append(str(curr))
		

	if co > cc:
		curr[pos] = ')'
		func(n,co,cc+1,curr,pos+1)

	if co < n:

		curr[pos] = '('
		func(n,co+1,cc,curr,pos+1)

n = int(input("Enter a no. : "))
curr = [" "] * (2*n)
l = list()
func(n,0,0,curr,0)

print(l)
for i in range(0,len(l)):
	for j in range(0,len(l[i])):
		print(l[i][j],end="")
	print()

