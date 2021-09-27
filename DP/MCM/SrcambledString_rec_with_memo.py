a = input()
b = input()


def substr(s,start,length):

	n = len(s)
	if (start + length) > n:
		raise Exception("Plz provide correct start and length")

	return s[start:(start + length)]

d = {}

def chk_scr(a,b):

	if len(a) != len(b):
		return False

	if a == b:
		return True

	s1 = a+" "+b
	s2 = b+" "+a
	if s1 in d.keys():
		return d[s1]
	if s2 in d.keys():
		return d[s2]

	n = len(a)

	for i in range(1,n):

		if chk_scr(substr(a,0,i),substr(b,0,i)) and chk_scr(substr(a,i,(n-i)),substr(b,i,(n-i))):
			d[s1] = True
			d[s2] = True
			return True

		if chk_scr(substr(a,0,i),substr(b,(n-i),i)) and chk_scr(substr(a,i,(n-i)),substr(b,0,(n-i))):
			d[s1] = True
			d[s2] = True
			return True

	d[s1] = False
	d[s2] = False
	return False

print(chk_scr(a,b))