def func(arr1,arr2):
    tot=len(arr1)+len(arr2)
    gap=tot/2
    if gap>int(tot/2):
        gap=int(tot/2)+1
    else:
        gap=int(gap)

    print(gap)

    while gap>0:
        print('gap-->',gap)
        index=0
        end_index=index+gap
        original_index=0
        original_end_index=0+gap
        print(index,end_index)
        flag_index=False
        flag_end_index=False

        while original_end_index<len(arr1)+len(arr2):
            if index>=len(arr1):
                index=index-len(arr1)
                flag_index=True
            if end_index>=len(arr1):
                end_index=end_index-len(arr1)
                flag_end_index=True

            print('index--> ',index,' end_index--> ',end_index)
            print('flag_index--> ',flag_index,' flag_end_index--> ',flag_end_index)
            if flag_index==False:
                if flag_end_index==False:
                    if arr1[index]>arr1[end_index]:
                        arr1[index],arr1[end_index]=arr1[end_index],arr1[index]
                    index+=1
                    end_index+=1
                    original_index+=1
                    original_end_index+=1
                    continue
                elif flag_end_index==True:
                    if arr1[index]>arr2[end_index]:
                        arr1[index],arr2[end_index]=arr2[end_index],arr1[index]
                    index+=1
                    end_index+=1
                    original_index+=1
                    original_end_index+=1
                    continue
            elif flag_index==True:
                if flag_end_index==True:
                    if arr2[index]>arr2[end_index]:
                        arr2[index],arr2[end_index]=arr2[end_index],arr2[index]
                    index+=1
                    end_index+=1
                    original_index+=1
                    original_end_index+=1
                    continue
                elif flag_end_index==False:
                    print('ERROR')
                    exit()

        gap=int(gap/2)

    print(arr1,arr2)

arr1=[1,4,7,8,10]
arr2=[2,3,9]
print(arr1,arr2)
func(arr1,arr2)