arr = [40,20,30,10,30]

def MCM(arr):
    n = len(arr)
    dp = list()

    for i in range(n+1):
        dp.append([-1]*(n+1))
    
    for i in range(0,n+1):
        for j in range(0,n+1):
            if i==0:
                dp[i][j]=float('inf')
            elif i>=j:
                dp[i-1][j] = 0

    for i in range(0,n+1):
        for j in range(0,n+1):
            print(dp[i][j],end='\t')
        print()

    for i in range(n-1,0,-1):
        for j in range(i+1,n+1):
            min_ = float('inf')
            for k in range(i,j+1):
                print(i,j,k)
                min_ = min(min_ , dp[i-2][k] + dp[k+1][j-1] + arr[i-2]*arr[k-1]*arr[j-2])

MCM(arr)