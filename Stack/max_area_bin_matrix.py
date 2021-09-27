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

	def nsl(self,arr):

		self.initialise()
		print(self.stk)
		op_list = []

		for i in range(0,len(arr)):

			if list(self.topf().keys())[0] < arr[i]:
				op_list.append(self.stk[self.top])
				self.push({arr[i]:i})

			else:

				while arr[i] <= list(self.topf().keys())[0]:
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

		print("nsl -->\n",op_list)
		return op_list


	def nsr(self,arr):

		self.initialise()
		print(self.stk)
		op_list = []

		for i in range(len(arr)-1,-1,-1):

			if list(self.topf().keys())[0] < arr[i]:
				op_list.append(self.stk[self.top])
				self.push({arr[i]:i})

			else:

				while arr[i] <= list(self.topf().keys())[0]:
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

		
		op_list2 = []
		for i in range(len(op_list)-1,-1,-1):
			op_list2.append(op_list[i])

		print("nsr -->\n",op_list2)
		return op_list2

def max_area_hist(arr):

	s1 = stack(10)
	s2 = stack(10)

	nsl_arr = s1.nsl(arr)
	nsr_arr = s2.nsr(arr)

	area_arr = [-1] * len(arr)
	print(area_arr)

	for i in range(len(arr)):

		if nsl_arr[i] == {-1:-1} and nsr_arr[i] == {-1:-1}:
			area_arr[i] = arr[i] * len(arr)

		elif nsl_arr[i] == {-1:-1}:
			key = list(nsr_arr[i].keys())[0]
			area_arr[i] = arr[i] * (nsr_arr[i][key] -1 - i + 1)

		elif nsr_arr[i] == {-1:-1}:
			key = list(nsl_arr[i].keys())[0]
			area_arr[i] = arr[i] * (i - nsl_arr[i][key] - 1 +1)

		else:
			keyl = list(nsl_arr[i].keys())[0]
			keyr = list(nsr_arr[i].keys())[0]
			area_arr[i] = arr[i] * (nsr_arr[i][keyr] -1 - nsl_arr[i][keyl] - 1 +1)


	return max(area_arr)



print("Enter row and column no :")
r,c = int(input()),int(input())
print("Enter matrix : ")
l = []

for i in range(r):
	l2 = [int(i) for i in input().split()]
	l.append(l2)

print(l)

building_arr = [[-1] * c] * r
print(building_arr)
for i in range(c):
	building_arr[0][i] = l[0][i]

max_area_list = [max_area_hist(building_arr[0])]
print("Max area list ---> ",max_area_list)

for i in range(1,r):
	for j in range(0,c):
		if l[i][j] == 0:
			building_arr[i][j] = 0
		else:
			building_arr[i][j] = l[i][j] + building_arr[i-1][j]
	print(building_arr)

	max_area_list.append(max_area_hist(building_arr[i]))

print(max_area_list)
print(max(max_area_list))
