def func(s,index,curr):

	if index == len(s):
		l.append(curr)
		return

	func(s,index+1,curr + chr(ord(s[index])-32))
	func(s,index+1,curr+s[index])

l = list()
s = input("Enter string : \n")
index = 0
curr = ""

func(s,index,curr)

print(l)