def minSwap (arr, k) : 
    #Complete the function
    good=0
    n=len(arr)
    print(arr)
    for i in arr:
        if i<=k:
            good+=1
            
    if good==0:
        return 0
        
    bad=0
    for i in range(0,good):
        if arr[i]>k:
            bad+=1
    
    for j in range(0,good):
        print(arr[j],end='  ')

    print()
        

    min_swaps=bad

    print('good--->',good)
    print('bad--->',bad)
    print()
    for i in range(1,n-good+1):
        
        print(arr[i-1])
        if arr[i-1]>k:
            bad-=1
        if arr[i+good-1]>k:
            bad+=1
        
        print('bad-->',bad)

        for j in range(i,i+good):
            print(arr[j],end='  ')

        print()
        min_swaps=min(min_swaps,bad)
        
    print(min_swaps)
    return min_swaps

arr=[4 ,16, 3 ,8 ,13 ,2 ,19, 4, 12, 2, 7, 17, 4, 19, 1]
k=9

minSwap(arr,k)

minSwap([20 ,3 ,5, 4, 14, 7, 11, 1, 9, 10, 3, 9],19)