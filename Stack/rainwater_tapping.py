class stack:

	def __init__(self,maxsize = 10):
		self.stk = [-1] * maxsize
		self.top = -1
		self.maxsize = maxsize

	def initialise(self):
		self.top += 1
		self.stk[self.top] = -1

	def push(self,val):
		if self.top == self.maxsize:
			print("Stack overflow")
			return

		self.top += 1
		self.stk[self.top] = val

	def pop(self):
		if self.top == -1:
			print("Stack underflow")
			return -1

		ele = self.stk[self.top]
		self.top -= 1
		return ele

	def topf(self):
		if self.top == -1:
			print("Stack underflow")
			return -1
		
		ele = self.stk[self.top]
		return ele

	def disp(self):

		t = self.top
		if t == -1:
			print("Stack underflow")
			return

		print(self.stk[0:self.top+1])


def mxr(arr):
	s = stack()
	s.initialise()
	op_list=[]
	for i in range(len(arr)-1,-1,-1):
		if s.topf() < arr[i]:
			s.push(arr[i])

	for i in arr:
		if i < s.topf():
			op_list.append(s.topf())
		elif i == s.topf():
			s.pop()
			op_list.append(s.topf())

	return op_list

def mxl(arr):
	s = stack()
	s.initialise()
	op_list=[]
	for i in range(0,len(arr)):
		if s.topf() < arr[i]:
			s.push(arr[i])

	for i in range(len(arr)-1,-1,-1):
		if arr[i] < s.topf():
			op_list.append(s.topf())
		elif arr[i] == s.topf():
			s.pop()
			op_list.append(s.topf())

	op_list2=[]
	for i in range(len(op_list)-1,-1,-1):
		op_list2.append(op_list[i])
	return op_list2

print("Enter array :")
arr = [int(i) for i in input().split()]
mxr_arr = mxr(arr)
mxl_arr = mxl(arr)

min_arr = []
ht = []
for i in range(len(arr)):
	min_arr.append(min(mxr_arr[i],mxl_arr[i]))
	if min_arr[i] >= arr[i]:
		ht.append(min_arr[i] - arr[i])

	else:
		ht.append(0)

print(mxr_arr)
print(mxl_arr)
print(min_arr)
print(ht)
print(sum(ht))
