def separate(arr):
    ptr1=0
    ptr2=0

    while ptr2<len(arr):
        if arr[ptr2]<0:
            arr[ptr1],arr[ptr2]=arr[ptr2],arr[ptr1]
            ptr1+=1
            ptr2+=1
        
        else:
            ptr2+=1

    return ptr1

def func(arr):
    index_of_separation = separate(arr)
    print(arr,index_of_separation)
    ptr1=1
    ptr2=index_of_separation

    while ptr1<len(arr) and ptr2<len(arr):
        print('ptr1-->',ptr1,' ptr2-->',ptr2)
        if arr[ptr1]<0:
            arr[ptr1],arr[ptr2]=arr[ptr2],arr[ptr1]
            ptr1+=2
            ptr2+=1
            print(arr)
        else:
            break

    print(arr)

arr=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
func(arr)
'''
arr=[1, 2, 3, -4, -1, 4]
print(arr)
func(arr)
'''