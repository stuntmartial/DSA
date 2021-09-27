x_moves = [2,2,1,1,-2,-2,-1,-2]
y_moves = [1,-1,2,-2,1,-1,2,-1]
count = 0
def get_next_move(board,i,j):
    global x_moves , y_moves

    min_deg = float('inf')
    min_deg_indices = [None,None]
    for x in range(len(x_moves)):
        nxt_move_deg = get_deg(i+x_moves[x],j+y_moves[x])
        if nxt_move_deg<min_deg:
            min_deg = nxt_move_deg
            min_deg_indices = [i+x_moves[x],j+y_moves[x]]

    return min_deg_indices

def isValid(i,j):
    if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
        return False
    else:
        return True

def is_Empty(board,i,j):
    if isValid(i,j) and board[i][j]<0:
        return True
    else:
        return False

def get_deg(i,j):
    global x_moves , y_moves

    if not isValid(i,j):
        return float('inf')
    
    deg=0
    for x in range(len(x_moves)):
        if is_Empty(board,i+x_moves[x],j+y_moves[x]):
            deg+=1
    return deg

def func(board,i,j):
    global count

    print('i: ',i,'j: ',j)
    if not isValid:
        return

    if board[i][j]!=0:
        return

    if board[i][j] == 0 and i==0 and j==0 and count!=0:
        return

    count+=1
    board[i][j] = count

    nxt_move_indices = get_next_move(board,i,j)
    print(nxt_move_indices)
    next_i , next_j = nxt_move_indices[0] , nxt_move_indices[1]

    func(board,next_i,next_j)

def disp(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end='  ')
        print()

N = 4
board = []
for i in range(N):
    board.append([0]*N)

#disp(board)
func(board,0,0)
disp(board)