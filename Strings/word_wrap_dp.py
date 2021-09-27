def word_wrap_dp(array,max_length):
    for i in array:
        if i>max_length:
            print('Cannot be accomodated...')
            break

    reference_array = [-1] * len(array)
    print('Current_words : ',[array[-1]])
    reference_array[-1] = (max_length - array[-1])**3
    print('cost>>>>',reference_array[-1])

    for index in range(len(array)-2,-1,-1):
        
        min_cost = float('inf')
        for i in range(index,len(array)):
            print('Current_words : ',array[index:i+1])
            curr_word_space = sum( array[index : i+1] )
            curr_words = i - index + 1
            curr_spaces = curr_words - 1
            curr_space_occupied = curr_word_space + curr_spaces

            if curr_space_occupied<=max_length:
                cost = (max_length - curr_space_occupied)**3 + reference_array[i+1]
                print('cost>>>>',cost)
                min_cost = min(cost,min_cost)
            else:
                print('Cannot be done')
                break

        reference_array[index] = min_cost 

    print(reference_array)

array = [3,2,2,5]
max_length = 6
word_wrap_dp(array,max_length)

