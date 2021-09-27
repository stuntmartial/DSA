Reference=list()

def word_wrap(arr,max_length):
    global Reference
    for i in arr:
        if i>max_length:
            print('Cannot be accomodated...')
            return -1

    Reference=[-1]*len(arr)
    #list_of_indices , 
    min_cost = word_wrap_util(arr=arr,index=0,max_length=max_length)
    print(min_cost)

def word_wrap_util(arr,index,max_length):
    global Reference
    print('Reference',Reference)
    print('Index called : ',index)
    if index > len(arr):
        return 0

    elif index==len(arr)-1:
        cost=(max_length-arr[index])**3
        Reference[index]=cost
        print('Reference:',Reference)
        print('Index finished:',index)
        return cost

    if Reference[index]!=-1:
        print('REFERRED')
        return Reference[index]

    cost = float('inf')
    for i in range(index,len(arr)):
        print('index:',index,'i:',i)
        curr_total_words_length = sum(arr[index:i+1])
        spaces = ((i-index)+1)-1
        curr_total_words_length += spaces

        if curr_total_words_length<=max_length:
            print('Calling i=',i)
            cost=min(cost,
                (max_length-curr_total_words_length)**3 + word_wrap_util(arr,index=i+1,max_length=max_length)
            )
        else:
            print('OVERFLOW')
            Reference[index]=cost
            print('Reference:',Reference)
            print('Index finished : ',index)
            return cost

arr=[3,2,2,5]
max_length=6
word_wrap(arr,max_length)