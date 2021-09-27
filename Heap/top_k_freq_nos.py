class min_const_heap:

	def __init__(self,arr,k):
		self.h = arr
		self.length = k

	def heapify(self):

		n= self.length - 1
		for i in self.h:

			j = i

			while True:
				k = 2*i+1
				l = 2*i+2

				if k<=n and l<=n:
					t = self.h[j]
					self.h[j] = min(self.h[j],self.h[k],self.h[l])
					if self.h[j]==t:
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
						self.h[k] = t
						j = l
						continue
					
				else:
					break

	def insert(self,val):

		if val > self.h[0]:
			return

		self.delete()
		self.length += 1
		self.h[self.length-1] = val
		i = self.length-1
		count = 1

		while True:
			j = i//2
			t = self.h[j]
			self.h[j] = min(self.h[i],self.h[j])
			if self.h[j] == t:
				break
			else:
				self.h[i] = t
				j = i
				if j == 0:
					count += 1
				if count == 2:
					break

	def delete(self):

		print("In self.delete")
		print("Heap before del ---->",self.h)

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


	def top_k_freq(self,arr,k):

		self.heapify()
		l = []
		for i in range(k,len(arr)):
			self.insert(arr[i])

		for i in range(k):
			l.append(self.h[0])
			self.delete()

		return l







print("Enter array :")
arr=[int(i) for i in input().split()]
k = int(input("Enter k : "))

freq_dict = {}
freq_list = []
for i in arr:
	try:
		freq_dict[i] += 1
	except:
		freq_dict[i] = 1

	
for i in freq_dict.keys():
	freq_list.append(freq_dict[i])

if len(arr) < k:
	print("Error")
	exit()

freq_dict_rev = {}
for i in freq_dict.keys():

	try:
		freq_dict_rev[freq_dict[i]].append(i)
	except:
		freq_dict_rev[freq_dict[i]] = [i]

for i in freq_dict_rev.keys():
	freq_dict_rev[i].sort()

print("freq_dict_rev--->",freq_dict_rev)


print(freq_dict)
print(freq_list)
h1 = min_const_heap(freq_list[0:k],k)
l = h1.top_k_freq(freq_list,k)
l2 = []
for i in range(len(l)-1,-1,-1):
	for j in freq_dict_rev[l[i]]:

		if j not in l2:
			l2.append(j)
			
		if len(l2) == k:
			break
print(l)
print(l2)