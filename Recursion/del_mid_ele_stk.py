class stack:

	def __init__(self,maxsize = 10):

		self.maxsize = maxsize
		self.top = -1
		self.stk = [-1] * maxsize
	
	def push(self,ele):

		if self.top == self.maxsize - 1:
			raise Exception("Stack overflow...")
			return

		self.top += 1
		self.stk[self.top] = ele

	def pop(self):

		if self.top == -1:
			raise Exception("Stack Underflow...")
			return

		temp = self.stk[self.top]
		self.top -= 1
		return temp

	def traverse(self):

		return self.stk[0:self.top +1]

def del_middle_ele(s,k,flag):

	if k == 0:
		s.pop()
		return

	temp = s.pop()
	del_middle_ele(s,k-1,flag)
	if flag == 'o': 
		s.push(temp)
	elif flag == 'e' and k!= 1:
		s.push(temp)

l = [int(i) for i in input().split()]
s = stack()
for i in l:
	s.push(i)


k = len(l) // 2
if len(l) %2 == 0:
	flag = 'e'
else:
	flag = 'o'
del_middle_ele(s,k,flag)
print(s.traverse())  