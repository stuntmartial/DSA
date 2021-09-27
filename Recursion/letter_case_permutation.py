digits = ['0','1','2','3','4','5','6','7','8','9']

def func(s,index,curr):

	if index == len(s):
		l.append(curr)
		return

	if s[index] in digits:

		func(s,index+1,curr+s[index])

	elif ord(s[index]) >= 65 and ord(s[index]) <= 90:

		func(s,index+1,curr + chr(ord(s[index]) +32))
		func(s,index+1,curr + s[index])

	elif ord(s[index]) >= 97 and ord(s[index]) <= 122:

		func(s,index+1,curr + chr(ord(s[index]) -32))
		func(s,index+1,curr+s[index])

l = list()
s = input("Enter string : \n")
index = 0
curr = ""

func(s,index,curr)

print(l)