count=0
def divide(arr,low,high):
    global count
    if low==high:
        return [arr[low]]

    mid=(low+high)//2
    left_arr=divide(arr,low,mid)
    right_arr=divide(arr,mid+1,high)
    
    print(left_arr,right_arr)
    new_arr=[]
    i=0
    j=0
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i]<=right_arr[j]:
            new_arr.append(left_arr[i])
            i+=1
        
        elif right_arr[j]<left_arr[i]:
            print(i,j)
            new_arr.append(right_arr[j])
            j+=1
            count+=(len(left_arr)-i)
            print('count++',count)
        
    while i<len(left_arr):
        new_arr.append(left_arr[i])
        i+=1

    while j<len(right_arr):
        new_arr.append(right_arr[j])
        j+=1

    return new_arr

arr=[5,3,2,4,1]
divide(arr,0,len(arr)-1)
print(count)
