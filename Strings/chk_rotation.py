def chk_rotation(str1,str2):
    str3=str1+str1

    if str2 in str3:
        return True
    else:
        return False

str1='abcde'
str2='cdeab'
op=chk_rotation(str1,str2)
print(op)