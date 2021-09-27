class stack:

	def __init__(self,maxsize = 1000):
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

	def ngr(self,arr):
		if self.top != -1:
			return

		self.initialise()
		self.disp()
		op_list = []

		for i in range(len(arr)-1,-1,-1):

			if arr[i] < self.topf():
				op_list.append(self.topf())
				self.push(arr[i])

			else:
				print(self.topf())
				while(self.topf() <= arr[i]):
					flag = self.pop()
					if flag == -1:
						break

				op_list.append(self.topf())
				self.push(arr[i])

		return [op_list[i] for i in range(len(op_list)-1,-1,-1)]

	def disp(self):

		t = self.top
		if t == -1:
			print("Stack underflow")
			return

		
		print(self.stk)

print("Enter array : ")
arr = [int(i) for i in input().split()]
s = stack(10)
l = s.ngr(arr)
print(l)