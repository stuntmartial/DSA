def word_wrap(arr,max_length):
    for i in arr:
        if i>max_length:
            print('Cannot be accomodated...')
            return -1

    #list_of_indices , 
    min_cost = word_wrap_util(arr=arr,index=0,max_length=max_length)
    print(min_cost)

def word_wrap_util(arr,index,max_length):
    if index > len(arr):
        return 0

    elif index==len(arr)-1:
        cost=(max_length-arr[index])**3
        return cost

    cost = float('inf')
    for i in range(index,len(arr)):
        curr_total_words_length = sum(arr[index:i+1])
        spaces = ((i-index)+1)-1
        curr_total_words_length += spaces

        if curr_total_words_length<max_length:
            cost=min(cost,
                (max_length-curr_total_words_length)**3 + word_wrap_util(arr,index=i+1,max_length=max_length)
            )
        else:
            return cost

arr=[3,2,2,5]
max_length=6
word_wrap(arr,max_length)