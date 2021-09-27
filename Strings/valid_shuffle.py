def valid_shuffle(str1,str2,result):
    ptr1=0
    ptr2=0
    ptr3=0

    while ptr3<len(result):
        print(ptr1,ptr2,ptr3)
        if ptr1<len(str1) and str1[ptr1]==result[ptr3]:
            ptr1+=1
            ptr3+=1
        elif ptr2<len(str2) and str2[ptr2]==result[ptr3]:
            ptr2+=1
            ptr3+=1
        else:
            return False

    if ptr1<len(str1) or ptr2<len(str2):
        return False
    else:
        return True

str1='xy'
str2='12'
result='1yx2'
op=valid_shuffle(str1,str2,result)
print(op)