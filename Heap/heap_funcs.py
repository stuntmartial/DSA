class heap:

	def __init__(self,arr):
		self.h = arr
		self.length = len(self.h)

	#create heap in o(n) time complexity
	def heapify(self):

		if self.length  == 0:
			return

		n = self.length - 1
		for i in range(n - 1,-1,-1):

			j = i
			while True:
				k = 2*j + 1
				l = 2*j + 2

				if k <= n and l <= n:

					t = self.h[j] 
					self.h[j] = max(self.h[j],self.h[k],self.h[l])

					if self.h[j] == t:
						break

					elif self.h[j] == self.h[k]:
						self.h[k] = t
						j = k
						continue

					elif self.h[j] == self.h[l]:
						self.h[l] = t
						j = l
						continue

				elif k <= n:

					t = self.h[j]
					self.h[j] = max(self.h[j],self.h[k])

					if self.h[j] == t:
						break

					elif self.h[j] == self.h[k]:
						self.h[k] = t
						j = k
						continue

				elif l <= n:

					t = self.h[j]
					self.h[j] = max(self.h[j],self.h[l])

					if self.h[j] == t:
						break

					elif self.h[j] == self.h[l]:
						self.h[l] = t
						j = l
						continue

				else:

					break

		return self.h

	def insert(self,val):

		self.length += 1
		self.h.append(val)
		i = (self.length - 1)
		j = (self.length - 1) //2 
		count = 0

		while j >= 0:
			
			if self.h[i] < self.h[j]:
				break

			elif self.h[i] > self.h[j]:
				t = self.h[j]
				self.h[j] = self.h[i]
				self.h[i] = t
				i = j
				j = j // 2
				if j == 0:
					count += 1
				if count == 2:
					break

		return self.h

	def ins2(self,val):
		
		#Clean written function for insertion...........!!!!!!!

		self.h.append(val)
		self.length+=1
		childIndex=self.length-1

		while childIndex!=0:
			parentIndex = (childIndex-1)//2
			if self.h[childIndex]<=self.h[parentIndex]:
				break
			else:
				self.h[parentIndex],self.h[childIndex]=self.h[childIndex],self.h[parentIndex]
				childIndex=parentIndex

	def delete(self):

		t = self.h[0]
		self.h[0] = self.h[self.length - 1]
		self.h[self.length - 1] = t
		self.length -= 1

		i = 0
		
		while True:


			j = i*2 + 1
			k = i*2 + 2
		
			if j <= self.length and k <=self.length:

				t = self.h[i]
				self.h[i] = max(self.h[i],self.h[j],self.h[k])

				if self.h[i] == t:
					break

				elif self.h[i] == self.h[j]:
					self.h[j] = t
					i = j
					continue

				elif self.h[i] == self.h[k]:
					self.h[k] = t
					i = k
					continue

			elif j<=self.length:

				t = self.h[i]
				self.h[i] = max(self.h[i],self.h[j])

				if self.h[i] == t:
					break

				elif self.h[i] == self.h[j]:
					self.h[j] == t
					i = j
					continue

			elif k<=self.length:

				t = self.h[i]
				self.h[i] = max(self.h[i],self.h[k])

				if self.h[i] == t:
					break

				elif self.h[i] == self.h[k]:
					self.h[k] == t
					i = k
					continue

			else:
				break

		return self.h[0:self.length]



# arr = [int(i) for i in input().split()]
# heap1 = heap(arr)
# print(heap1.heapify())
# print(heap1.insert(int(input("Enter no :"))))
# print(heap1.delete())
# print(heap1.delete())

heap1=heap([])
heap1.ins2(22)
heap1.ins2(1)
heap1.ins2(13)
heap1.ins2(32)
heap1.ins2(42)
heap1.ins2(50)
print(heap1.h)