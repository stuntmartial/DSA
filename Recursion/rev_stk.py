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


def rev_stack(s,n):

	if n == 1 :
		return s

	temp = s.pop()
	rev_stack(s,n-1)
	insert(s,temp)

def insert(s,ele):

	if len(s.traverse()) == 0:
		s.push(ele)

	else:
		temp = s.pop()
		insert(s,ele)
		s.push(temp)

l = [int(i) for i in input().split()]
s = stack()
for i in l:
	s.push(i)

n = len(l)

rev_stack(s,n)
print(s.traverse())