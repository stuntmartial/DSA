count=0
def func(board,i,j):

	global count
	if i>=n or j>=n or i<0 or j<0:
		return
	if board[i][j]!=0:
		return
	if board[i][j]==0 and i==0 and j==0 and count!=0:
		return

	board[i][j]=count
	count+=1

	func(board,i+2,j+1)
	func(board,i+2,j-1)
	func(board,i-2,j+1)
	func(board,i-2,j-1)

	func(board,i+1,j+2)
	func(board,i+1,j-2)
	func(board,i-1,j+2)
	func(board,i-1,j-2)

n=int(input("Enter n: "))
board=[]
for i in range(n):
	board.append([0]*n)
#print(board)
func(board,0,0)
for i in range(n):
	for j in range(n):
		print(board[i][j],"\t",end="")
	print()