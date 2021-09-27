def find_count(matrix,ele):
    count=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]<=ele:
                count+=1
    return count

def find_median(matrix):
    min_=float('inf')
    max_=float('-inf')

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            min_=min(min_,matrix[i][j])
            max_=max(max_,matrix[i][j])


    desired=(len(matrix)*len(matrix[0])+1)//2

    while min_<max_:
        mid=min_+ (max_-min_)//2

        count=find_count(matrix,mid)

        if count<desired:
            min_=mid+1
        else:
            max_=mid

    print('Median is : ',min_)

matrix=[[1,4,7],[2,7,9],[3,7,9]]
find_median(matrix)