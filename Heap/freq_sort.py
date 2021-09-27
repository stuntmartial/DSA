class min_heap:

	def __init__(self,arr):
		self.h = arr
		self.length = len(arr)

	def heapify(self):

		n = self.length - 1
		for i in self.h:

			j = i
			while True:
				k = 2*j+1
				l = 2*j+2

				if k<=n and j<=n:
					t=self.h[j]
					self.h[j] = min(self.h[j],self.h[k],self.h[l])
					if self.h[j]==t:
						break
					elif self.h[j] == self.h[k]:
						self.h[k]=t
						j=k
						continue
					elif self.h[j] == self.h[l]:
						self.h[l]=t
						j=l
						continue

				elif k<=n:
					t=self.h[j]
					self.h[j] = min(self.h[j],self.h[k])
					if self.h[j]==t:
						break
					elif self.h[j]==self.h[k]:
						self.h[k]=t
						j=k
						continue
				elif l<=n:
					t=self.h[j]
					self.h[j] = min(self.h[j],self.h[l])
					if self.h[j]==t:
						break
					elif self.h[j]==self.h[l]:
						self.h[l]=t
						j=l
						continue
				else:
					break

	def delete(self):

		t=self.h[0]
		self.h[0] = self.h[self.length-1]
		self.length -= 1
		n = self.length-1
		j = 0
		while True:
			k = 2*j+1
			l = 2*j+2

			if k<=n and j<=n:
				t=self.h[j]
				self.h[j] = min(self.h[j],self.h[k],self.h[l])
				if self.h[j]==t:
					break
				elif self.h[j] == self.h[k]:
					self.h[k]=t
					j=k
					continue
				elif self.h[j] == self.h[l]:
					self.h[l]=t
					j=l
					continue

			elif k<=n:
				t=self.h[j]
				self.h[j] = min(self.h[j],self.h[k])
				if self.h[j]==t:
					break
				elif self.h[j]==self.h[k]:
					self.h[k]=t
					j=k
					continue
			elif l<=n:
				t=self.h[j]
				self.h[j] = min(self.h[j],self.h[l])
				if self.h[j]==t:
					break
				elif self.h[j]==self.h[l]:
					self.h[l]=t
					j=l
					continue
			else:
				break

	def freq_sort(self):

		l = []
		self.heapify()
		for i in range(self.length):
			l.append(self.h[0])
			self.delete()

		return l



print("Enter array : ")
arr = [int(i) for i in input().split()]
freq_list = []
freq_dict = {}
for i in arr:
	try:
		freq_dict[i] += 1
	except:
		freq_dict[i] = 1

for i in freq_dict:
	freq_list.append(freq_dict[i])

h=min_heap(freq_list)
l = h.freq_sort()
print(l)

freq_dict_rev = {}
for i in freq_dict.keys():

	try:
		freq_dict_rev[freq_dict[i]].append(i)
	except:
		freq_dict_rev[freq_dict[i]] = [i]


print("freq_dict_rev--->",freq_dict_rev)
l2=[]
for i in range(0,len(l)):
	for j in freq_dict_rev[l[i]]:

		if j not in l2:
			l2.append(j)
			
		
print(l2)