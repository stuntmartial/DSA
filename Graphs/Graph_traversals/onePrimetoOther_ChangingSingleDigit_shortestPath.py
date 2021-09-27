class Graph:
	def __init__(self):
		self.nodes=0
		self.edges=0
		self.d={}

	def add_node(self,node):
		if node not in self.d.keys():
			self.d[node]=[]
			self.nodes+=1

	def add_edge(self,node1,node2):
		if node1 not in self.d.keys():
			self.add_node(node1)
		if node2 not in self.d.keys():
			self.add_node(node2)

		if node2 not in self.d[node1]:
			self.d[node1].append(node2)
		if node1 not in self.d[node2]:
			self.d[node2].append(node1)
		self.edges+=1

	def bfs(self,source,destination):
		q=[]
		visited_dict={v:0 for v in self.d.keys()}
		parent_dict={v:None for v in self.d.keys()}
		q.append(source)
		visited_dict[source]=1
		parent_dict[source]=None
		flag=0

		while len(q)>0:
			v=q.pop(0)
			for i in self.d[v]:
				if visited_dict[i]==0:
					q.append(i)
					visited_dict[i]=1
					parent_dict[i]=v
					if i==destination:
						flag=1
						break
			if flag==1:
				break

		v=destination
		rev_path=[]
		rev_path.append(destination)
		while parent_dict[v]!=None:
			v=parent_dict[v]
			rev_path.append(v)
		path=[]
		for i in range(len(rev_path)-1,-1,-1):
			path.append(rev_path[i])

		return path

def SOE_4digit():
	n=10000
	prime_no_list=[]
	prime_no_dict={i:True for i in range(2,n)}
	no=int(n**(0.5))
	for i in range(2,no):
		if isPrime(i):
			for j in range(i**2,n):
				if j%i==0:
					prime_no_dict[j]=False

	for i in range(1000,n):
		if prime_no_dict[i]==True:
			prime_no_list.append(i)

	print(prime_no_list)
	print(no)
	return prime_no_list

def isPrime(val):
	flag=1
	for i in range(2,val//2):
		if val%i==0:
			flag=0
			break

	return flag

def isvalid(num1,num2):
	n1=str(num1)
	n2=str(num2)
	count=0
	if n1[0]!=n2[0]:
		count+=1 
	if n1[1]!=n2[1]:
		count+=1 
	if n1[2]!=n2[2]:
		count+=1 
	if n1[3]!=n2[3]:
		count+=1 
	
	if count==1:
		return 1
	else:
		return 0

def find_shortest_path(num1,num2):
	g=Graph()
	prime_no_list=SOE_4digit()
	for i in range(len(prime_no_list)):
		for j in range(i+1,len(prime_no_list)):
			if isvalid(prime_no_list[i],prime_no_list[j]):
				g.add_edge(prime_no_list[i],prime_no_list[j])

	print(g.d[1033])

	path=g.bfs(num1,num2)
	print(path)

num1,num2=int(input("Enter num1 : ")),int(input("Enter num2 : "))
find_shortest_path(num1,num2)
#SOE_4digit()
'''
print(isPrime(num1))
print(isPrime(num2))
'''