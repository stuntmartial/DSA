def func(arr):
    if arr[0]==0:
        return float('inf')

    n=len(arr)
    jumps=[float('inf')]*n

    jumps[n-1]=0
    print(jumps)
    for i in range(n-2,-1,-1):
        print('i----->',i)
        if arr[i]==0:
            jumps[i]=float('inf')

        elif i+arr[i]>=n-1:
            jumps[i]=1

        else:
            min_=float('inf')
            for j in range(i+1,n):
                
                if j<=i+arr[i]:
                    jump=jumps[j]
                    if jump!=float('inf') and jump<min_:
                        min_=jump

            if min_!=float('inf'):
                jumps[i]=min_+1

        print(jumps)

    print(jumps)
    return jumps[0]

arr=[1,3,6,1,0,9]
min_=func(arr)
print(min_)