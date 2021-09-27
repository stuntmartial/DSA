def split(str1):
    count_0=0
    count_1=0
    list_of_indices=list()

    for i in range(len(str1)):
        if str1[i]=='0':
            count_0+=1
        elif str1[i]=='1':
            count_1+=1

        if count_0==count_1:
            list_of_indices.append(i)

    if count_0!=count_1:
        return -1
    else:
        list_of_indices.insert(0,-1)
        return list_of_indices
    
str1="0100110101"
str2="0111100010"
str3="01000000010"
indices=split(str2)
if indices==-1:
    print(indices)
else:
    print(indices)
    for i in range(len(indices)-1):
        print(str2[indices[i]+1:indices[i+1]+1])