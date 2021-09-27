# upto 5 places

def getNthroot(n,m):
    low=0
    high=m
    diff=1e-6

    while high-low>=diff:
        mid = low+(high-low)/2
        estimatedNum = mid**n 
        
        print('low--->',low,'high--->',high,'mid--->',mid,'estimatedNum--->',estimatedNum)
        if estimatedNum==m:
            return mid

        elif estimatedNum<m:
            res = mid
            low = mid
        
        elif estimatedNum>m:
            high=mid

    res = res * 10**5 #d digits after decimal
    res = int(res)
    res = res/10**5

    print(res)

getNthroot(2,27)