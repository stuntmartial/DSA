def minPath(arr):

    sp=[]
    for i in range(len(arr)):
        sp.append([-1]*len(arr[0]))

    disp(sp)
    
    for i in range(len(sp)):
        for j in range(len(sp[0])):
            if i==0 and j==0:
                sp[i][j]=arr[i][j]
            elif j==0:
                sp[i][j]=sp[i-1][j]+arr[i][j]
            elif i==0:
                sp[i][j]=sp[i][j-1]+arr[i][j]
    disp(sp)
    
    for i in range(1,len(sp)):
        for j in range(1,len(sp[0])):
            sp[i][j]=min(sp[i-1][j],sp[i][j-1],sp[i-1][j-1])+arr[i][j]

    disp(sp)
    
def disp(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j],end='\t')
        print()

    print()

arr=[
[1,2,3],
[4,8,2],
[1,5,3]
]

minPath(arr)