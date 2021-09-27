def getId(m,n):
    
    flag2=0
    for i in range(2):
        for j in range(n):
            if m[i][j] == 1:
                flag2=1
                break
           
    if flag2==0:
        return -1
        
    l = []
    for i in range(n):
        l.append(i)
    id_=-1
    for i in range(0,len(l)):
        if len(l)==1:
            break
        f=l.pop(len(l)-1)
        s=l.pop(len(l)-1)
    
        if m[f][s] == 1:
            id_=s
            l.append(s)
        else:
            id_=f
            l.append(f)
        
    flag=0
    for i in range(0,n):
        if m[id_][i]==1:
            flag=1
            break

    if flag==1:
        return -1
    else:
        return id_


print("Enter n :")
n=int(input())
a=[]
for i in range(n):
    l=[int(i) for i in input().split()]
    a.append(l)

print(a)

print(getId(a,n))