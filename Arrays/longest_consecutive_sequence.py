def func(arr):
    ht={i:True for i in arr}
    max_=float('-inf')
    for i in range(len(arr)):
        curr_seq_length=1
        try:
            if ht[arr[i]-1]==True:
                continue
        except:
            j=arr[i]
            while True:
                j+=1
                try:
                    if ht[j]==True:
                        curr_seq_length+=1
                except:
                    max_=max(max_,curr_seq_length)
                    break

    print(max_)

arr=[1,9,3,10,4,20,2,11,12,13,14]
func(arr)