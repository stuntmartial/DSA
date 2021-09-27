print("Enter dimnensions : ")
(r,c) = int(input()),int(input())
print("Enter 2d array :")
arr = list()

for i in range(0,r):

	k = [int(i) for i in input().split()]
	assert len(k) == c
	arr.append(k)

ele = int(input("Enter element : "))

i = 0
j = c - 1
flag = 0



while (i >= 0 and i < r) and (j >= 0 and j < c):
	

	if arr[i][j] == ele:
		flag = 1
		break

	elif arr[i][j] < ele:
		i+=1

	else: 
		j-=1

if flag == 1:
	print(i,"\t",j)

elif flag == 0:
	print("Element not found")