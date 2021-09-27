class stack:

	def __init__(self,maxsize=10):
		self.stk=[1000000]*maxsize
		self.top=-1
		self.maxsize=maxsize

	def initialise(self):
		self.top+=1

	def push(self,val):
		if self.top==self.maxsize:
			print("Stack overflow")
			return

		self.top+=1
		self.stk[self.top]=val

	def pop(self):
		if self.top==-1:
			print("Stack underflow")
			return

		ele=self.stk[self.top]
		self.top-=1
		return ele

	def topf(self):
		if self.top==-1:
			print("Stack underflow")
			return

		ele=self.stk[self.top]
		return ele

	def disp(self):
		if self.top==-1:
			print("Stack underflow")
			return

		return self.stk[0:self.top+1]

print("Enter arr")
arr=[int(i) for i in input().split()]
s1=stack()
s2=stack()
s2.initialise()
for i in range(len(arr)-1,-1,-1):
	s1.push(arr[i])
	
for i in arr:
	if s2.topf()>i:
		s2.push(i)
	
print(s1.disp())
print(s2.disp())

#Stack is displayed : left -> right : 0 -> self.top
