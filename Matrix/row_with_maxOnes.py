def get_index(arr):
    low=0
    high=len(arr)

    while low<high:
        mid=low+(high-low)//2
        if arr[mid]==0:
            low=mid+1
        elif arr[mid]==1:
            high=mid

    return low

def func(matrix):
    max_index=get_index(matrix[0])
    max_row=0

    for i in range(1,len(matrix)):
        if matrix[i][max_index]!=1:
            continue
        index=get_index(matrix[i][0:max_index])
        if index<max_index:
            max_index=index
            max_row=i

    print('Required row : ',max_row)

matrix=[[0, 0, 0, 1], [0, 1, 1, 1],[1, 1, 1, 1], [0, 0, 0, 0]]
func(matrix) 