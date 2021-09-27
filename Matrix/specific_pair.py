def func(matrix):
    precomp_matrix=[([0]*len(matrix[0]))]*len(matrix)
    n=len(matrix)
    precomp_matrix[n-1][n-1]=matrix[n-1][n-1]
    max_val=float('-inf')

    for i in range(n-2,-1,-1):
        precomp_matrix[n-1][i]=max(matrix[n-1][i],precomp_matrix[n-1][i+1])
    
    for i in range(n-2,-1,-1):
        precomp_matrix[i][n-1]=max(matrix[i][n-1],precomp_matrix[i+1][n-1])

    for i in range(n-2,-1,-1):
        for j in range(n-2,-1,-1):
            if precomp_matrix[i+1,j+1]-matrix[i][j] > max_val:
                max_val=precomp_matrix[i+1,j+1]-matrix[i][j]
            precomp_matrix[i][j]=max(arr[i][j],max(max(precomp_matrix[i+1][j])+max(precomp_matrix[i][j+1])))

matrix=[[ 1, 2, -1, -4, -20 ],
[ -8, -3, 4, 2, 1 ], 
[ 3, 8, 6, 1, 3 ],
[ -4, -1, 1, 7, -6 ],
[ 0, -4, 10, -5, 1 ]]

func(matrix)