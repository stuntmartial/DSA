def out_of_place(element,index):
    if index%2==0:
        if element>0:
            return True
        else:
            return False

    else:
        if element<0:
            return True
        else:
            return False

def get_sign(element):
    if element<0:
        return '-ve'
    else:
        return '+ve'

def func(arr):
    ptr1=None
    ptr2=None

    for i in range(0,len(arr)):
        if out_of_place(arr[i],i):
            ptr1=arr[i]
            sign=get_sign(arr[i])
            flag=0
            
            for j in range(i+1,len(arr)):
                if get_sign(arr[j]) != get_sign(arr[i]):
                    flag=1
                    break
            
            if flag==0:
                break

            temp=arr[j]
            for k in range(j,i-1,-1):
                arr[k]=arr[k-1]

            arr[i]=temp
        print(arr)

    print(arr)

arr=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(arr)
func(arr)
arr2=[1, 2, 3, -4, -1, 4]
print(arr2)
func(arr2)