def func(arr):
    arr.sort()
    print(arr)

    op_arr=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i][0]>=op_arr[len(op_arr)-1][0] and arr[i][0]<op_arr[len(op_arr)-1][1]:
            if arr[i][1]>op_arr[len(op_arr)-1][1]:
                op_arr[len(op_arr)-1][1]=arr[i][1]

        else:
            op_arr.append(arr[i])

    print(op_arr)

arr=[ [6,8], [1,2], [2,4], [4,7] ]
func(arr)