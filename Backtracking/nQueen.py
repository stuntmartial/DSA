def disp(board):
	global n
	for i in range(n):
		for j in range(n):
			print(board[i][j],end="")
		print()

def func(board,row):

	global n
	if row >= n:
		return True

	for i in range(n):
		print("i value in row ",row," is ",i)
		if issafe(board,row,i):
			print(row,i," is safe")
			board[row][i]=1
			print(board)

			if func(board,row+1) ==True:
				return True

			board[row][i] = 0
		else:
			print(row,i," is not safe")

	return False

def issafe(board,row,column):

	for i in range(0,row):
		if board[i][column] == 1:
			return False

	for i,j in zip(range(row-1,-1,-1),range(column-1,-1,-1)):
		if board[i][j] == 1:
			return False

	for i,j in zip(range(row-1,-1,-1),range(column+1,n)):
		if board[i][j] == 1:
			return False

	return True

global n
n = int(input("Enter N : "))
board=[]
for i in range(n):
	board.append([0]*n)
print(board)
func(board,0)
disp(board)