def func(arr1,arr2):
    if arr1==None:
        return arr2
    elif arr2==None:
        return arr1

    i=j=0

    while i<len(arr1) and j<len(arr2):
        print(i,j)
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            temp=arr1[i]
            arr1[i]=arr2[j]
            arr2.pop(j)
            k=0
            print(arr2[k])
            while k<len(arr2) and temp>arr2[k]:
                k+=1

            if k<len(arr2):
                arr2.insert(k,temp)

            elif k==len(arr2):
                arr2.append(temp)
            
        elif arr1[i]==arr2[j]:
            i+=1
            j+=1

        print(arr1,arr2)

arr1=[1,4,7,8,10]
arr2=[2,3,9]
func(arr1,arr2)