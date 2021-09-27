def func(arr):

    #right_to_left_pass
    first_transaction_profs=[0] * len(arr)
    max_right=arr[len(arr)-1]

    for i in range(len(arr)-2,-1,-1):
        first_transaction_profs[i] = max(first_transaction_profs[i+1] , max_right-arr[i])
        max_right=max(max_right,arr[i])

    print(first_transaction_profs)

    #left_to_right_pass
    second_transaction_profs=[0] * len(arr)
    second_transaction_profs[0]=first_transaction_profs[0]
    min_left=arr[0]

    for i in range(1,len(arr)):
        second_transaction_profs[i]=max(first_transaction_profs[i]+arr[i]-min_left , second_transaction_profs[i-1])
        min_left=min(min_left,arr[i])

    print(second_transaction_profs)
    print('Maximum prof : ',second_transaction_profs[len(second_transaction_profs)-1])


arr=[2,4,2,6,2,3]
func(arr)

arr=[5,4,3,2]
func(arr)