class max_const_heap:

	def __init__(self,arr,k):

		self.h = arr
		self.length = k

	def heapify(self):

		n = self.length - 1

		for i in range(0,n):

			j = i
			while True:	
				k = 2*j+1
				l = 2*j+2

				if k<=n and l<=n:
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

				elif k<=n:
					t = self.h[j]
					self.h[j] = max(self.h[j],self.h[k])
					if self.h[j] == t:
						break
					elif self.h[j] == self.h[k]:
						self.h[k] = t
						j = k
						continue

				elif l<=n:
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

	def insert(self,val):

		print("Inserting ",val)
		if val > self.h[0]:
			return

		self.delete()
		self.length += 1
		self.h[self.length-1] = val
		
		count = 1
		i = self.length-1
		print("heap before swap attempts -->",self.h)
		while  True:
			j = i//2
			if self.h[j] > self.h[i]:
				break

			else:
				t = self.h[j]
				self.h[j] = max(self.h[j],self.h[i])
				if self.h[j] == t:
					break
				elif self.h[j] == self.h[i]:
					self.h[i] = t
					i = j
					if j == 0:
						count+=1
					if count == 2:
						break
		print("heap after insertion ",self.h)

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

			
				elif k<=n:

					t = self.h[j]
					self.h[j] = max(self.h[j],self.h[k])
					if self.h[j] == t:
						break
					elif self.h[j] == self.h[k]:
						self.h[k] = t
						j = k
						continue

				elif l<=n:

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

		print("Heap after deleting --->",self.h[0:self.length])

	def k_closest(self,arr,ele,k):

		self.heapify()
		print("heap after heapify ---->",self.h)
		for i in range(k,len(arr)):
			self.insert(diff_list[i])

		print("heap ---> ",self.h)

		l = list()
		for i in self.h:
			l.append(self.h[0])
			self.delete()

		return l



print("Enter array : ")
arr = [int(i) for i in input().split()]
k = int(input("Enter k : "))
ele = int(input("Enter ele : "))

if k > len(arr):
	print("k is more than length of array")
	exit()


diff = {abs(ele-i):[] for i in arr}
diff_list = []
for i in arr:

	diff[abs(i-ele)].append(i)
	diff_list.append(abs(i-ele))

print(diff,"\n",diff_list)

h1 = max_const_heap(diff_list[0:k],k)
l = h1.k_closest(diff_list,ele,k)

l2 = []
flag = 0
for i in range(len(l)-1,-1,-1):
	for j in diff[l[i]]:
		if j not in l2:
			l2.append(j)
		if len(l2) == k:
			flag = 1
			break
	if flag == 1:
		break


print(l)
print(l2)



