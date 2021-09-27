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


print("Enter array: ")
arr=[int(i) for i in input().split()]
encoded_stk=stack()
encoded_stk.push(arr[0])

min_ele = arr[0]
for i in range(1,len(arr)):

	if arr[i]<min_ele:
		encoded_stk.push(2*arr[i]-min_ele)
		min_ele=arr[i]
	else:
		encoded_stk.push(arr[i])

print(encoded_stk.disp())
print(min_ele)

for i in range(len(arr)-1,-1,-1):

	stop = encoded_stk.topf()
	if stop>min_ele:
		print(stop,"  ",min_ele)
		encoded_stk.pop()

	else:
		print(stop,"  ",min_ele)
		min_ele=2*arr[i]-encoded_stk.pop()



