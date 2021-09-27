dp=[]
def func(arr,start,end):
    global dp
    print(start,end)
    if start==end:
        return 0

    if dp[start][end] is not None:
        print('Used')
        return dp[start][end]

    if arr[start]==0:
        dp[start][end]=float('inf')
        return float('inf')

    min_=float('inf')
    for i in range(start+1,end+1):
        if i <= start+arr[start]:
            jump=func(arr,i,end)
            if jump!=float('inf') and jump<min_:
                min_=jump

    min_=1+min_
    dp[start][end]=min_
    return min_

def utility(arr):
    global dp
    n=len(arr)
    for i in range(n):
        dp.append([None]*n)
    '''
    for i in range(n):
        for j in range(n):
            print('(',i,',',j,')',end='\t')
        print()
    '''

arr=[1,3,6,1,0,9]
if arr[0]==0:
    print('inf')
    return
utility(arr)
min_=func(arr,0,len(arr)-1)
print(min_)
print(dp)