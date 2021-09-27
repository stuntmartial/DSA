def func(s,index,curr):

	if index == len(s):
		l.append(curr)
		return 

	func(s,index+1,curr + "_" + s[index])
	func(s,index+1,curr + s[index])

l = list()
s = input("Enter a string : \n")
if len(s) == 0:
	print("")
	exit()

index = 0
curr = ""

func(s[1:len(s)] , index,curr)

for i in range(0,len(l)):
	l[i] = s[0] + l[i]

print(l)