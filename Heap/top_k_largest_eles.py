class min_const_heap:

	def __init__(self,arr,k):
		self.h = arr
		self.length = k
		print("Heap -->",self.h)

	def heapify(self):

		n = self.length-1 

		for i in range(n-1,-1,-1):

			j = i
			while True:

				k = 2*j+1
				l = 2*j+2

				if k<=n and l<=n:

					t = self.h[j]
					self.h[j] = min(self.h[j],self.h[k],self.h[l])
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

			
				elif k<=n:

					t = self.h[j]
					self.h[j] = min(self.h[j],self.h[k])
					if self.h[j] == t:
						break
					elif self.h[j] == self.h[k]:
						self.h[k] = t
						j = k
						continue

				elif l<=n:

					t = self.h[j]
					self.h[j] = min(self.h[j],self.h[l])
					if self.h[j] == t:
						break
					elif self.h[j] == self.h[l]:
						self.h[l] = t
						j = l
						continue
					
				else:
					break

		print("Heap after heapify ---->",self.h)

	def insert(self,val):

		if val<=self.h[0]:
			return

		else:
			print("Inserting ",val)
			self.delete()
			self.h[self.length] = val
			self.length += 1
			count = 1

			i = self.length-1
			while True:

				if count == 2:
					break

				j = i//2
				t = self.h[j]
				self.h[j] = min(self.h[i],self.h[j])
				if self.h[j] == t:
					break
				else:
					self.h[i] = t
					i = j
					if j == 0:
						count += 1

				
		print("Heap ---->",self.h)

	def delete(self):

		print("In self.delete")

		t = self.h[0]
		self.h[0] = self.h[self.length-1]
		self.length -= 1
		n = self.length-1
		j = 0
		while True:

				k = 2*j+1
				l = 2*j+2

				if k<=n and l<=n:

					t = self.h[j]
					self.h[j] = min(self.h[j],self.h[k],self.h[l])
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

			
				elif k<=n:

					t = self.h[j]
					self.h[j] = min(self.h[j],self.h[k])
					if self.h[j] == t:
						break
					elif self.h[j] == self.h[k]:
						self.h[k] = t
						j = k
						continue

				elif l<=n:

					t = self.h[j]
					self.h[j] = min(self.h[j],self.h[l])
					if self.h[j] == t:
						break
					elif self.h[j] == self.h[l]:
						self.h[l] = t
						j = l
						continue
					
				else:
					break

		print("Heap after deleting --->",self.h[0:self.length])
		return t




	def top_k(self,arr,k):

		l = []
		self.heapify()

		for i in arr[k:len(arr)]:

			print("i--->",i)
			if i < self.h[0]:
				continue

			else:
				self.insert(i)

		print("Enter deleting loop")
		for i in self.h:
			l.append(self.h[0])
			self.delete()
			

		return l 



print("Enter array :")
arr = [int(i) for i in input().split()]
k = int(input("Enter k :"))

if k > len(arr):
	print("k is more than length of array")
	exit()

h1 = min_const_heap(arr[0:k],k)
l = h1.top_k(arr,k)
print(l)