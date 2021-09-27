def func(s):
    print(s)
    if len(s)==0 or len(s)==1:
        return s

    if s[0]==s[1]:

        while len(s)>1 and s[0]==s[1]:
            s=s[1:]
            
        s=s[1:]
        print('s:',s)
        return func(s)

    rem_s = func(s[1:])

    if len(rem_s)!=0 and rem_s[0]==s[0]:
        return rem_s[1:]
    
    elif len(rem_s)==0:
        return s[0]

    return s[0]+rem_s

s = 'acbbcddc'
print(func(s))