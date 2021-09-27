def LPS(string):
    
    LPS_array = [0] * len(string)

    if len(string)==1:
        print([0])
        return [0]

    i = 1
    required_pos = 0
    n = len(string)
    
    while i<n:
        if string[required_pos] == string[i]:
            LPS_array[i] = required_pos+1
            required_pos += 1
            i+=1

        else:
            if required_pos>0:
                required_pos = LPS_array[required_pos-1]
            else:
                LPS_array[i]=0
                i+=1
    
    print(LPS_array)
    return LPS_array


def KMP(string,pattern):
    if len(pattern)>len(string):
        return -1
    
    new_string = pattern + '#' + string
    print('new_string---->',new_string)
    pattern_length = len(pattern)

    lps_array = LPS(new_string)     
    print(lps_array)
    indices = list()
    count_of_substrings = 0

    for i in range(len(lps_array)):
        if lps_array[i] == pattern_length:
            indices.append(i)
            count_of_substrings += 1

    print(indices)
    print(count_of_substrings)
    
#string = "aabaacaabaad"
#LPS(string)
string1 = "ababa"
pattern1 = "aba"
KMP(string1,pattern1)
