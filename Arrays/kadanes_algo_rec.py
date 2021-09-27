max_=-99999
def func(arr,index):
    global max_
    if index==0:
        k=arr[index]
        max_=arr[index]
        return k

    else:
        k=max(func(arr,index-1)+arr[index] , arr[index] ) 
        max_=max(max_,k)
        return k

arr=[-2, -3, 4, -1, -2, 1, 5, -3]
func(arr,len(arr)-1)
print(max_)