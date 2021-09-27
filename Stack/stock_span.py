class stack:

	def __init__(self,maxsize = 100):
		self.stk = [{-1:-1}]*maxsize
		self.top = -1
		self.maxsize = maxsize

	def initialise(self):
		self.top += 1  

	def push(self,val):
		if self.top == self.maxsize:
			print("stack overflow")
			return

		self.top+=1
		self.stk[self.top] = val

	def pop(self):
		if self.top==-1:
			print("stack underflow")
			return {-1:-1}

		ele = self.stk[self.top]
		self.top-=1
		return ele

	def topf(self):
		if self.top == -1:
			print("Stack underflow")
			return {-1:-1}

		return self.stk[self.top]

	def stock_span(self,arr):

		self.initialise()
		print(self.stk)
		op_list = []

		for i in range(0,len(arr)):

			if list(self.topf().keys())[0] > arr[i]:
				op_list.append(self.stk[self.top])
				self.push({arr[i]:i})

			else:

				while arr[i] >= list(self.topf().keys())[0]:
					flag = self.pop()
					if flag == {-1:-1}:
						break
					print(list(self.topf().keys())[0])

				op_list.append(self.stk[self.top])
				self.push({arr[i]:i})

		l = []
		for i in range(len(op_list)):
			key = list(op_list[i].keys())[0]
			if i ==0 and op_list[i][key] == -1:
				l.append(-1)
			elif op_list[i][key] == -1:
				l.append(i+1)
			else:
				l.append(i - op_list[i][key] )

		print(op_list)
		print(l)

print("Enter array :")
arr = [int(i) for i in input().split()]
s = stack(10)
s.stock_span(arr)