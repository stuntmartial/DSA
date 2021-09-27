def ps(s,index,curr):

	if index == len(s):
		l.append(curr)
		return

	ps(s,index+1,curr)
	ps(s,index+1,curr+s[index])

l = list()
s = input("Enter a string")
index = 0
curr = ""

ps(s,index,curr)

#l=sorted(l)

print(l)