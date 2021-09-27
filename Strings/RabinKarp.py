#To be corrected.....

ht=dict()
for i in range(0,26):
    ht[chr(97+i)] = i+1

print(ht)

def RabinKarp(string,pattern):
    global ht

    if string=="" and pattern=="":
        return 0

    count = 0
    indices = list()
    total_chars = 256
    window_size = len(pattern)
    pattern_hash_val = 0

    for i in range(0,window_size):
        pattern_hash_val += ht[pattern[i]] * (total_chars ** window_size-1-i)

    string_window_hash_val = 0

    for i in range(0,window_size):
        string_window_hash_val += ht[string[i]] * (total_chars ** window_size-1-i)

    if pattern_hash_val == string_window_hash_val:
        count += 1
        indices.append(0)

    print(pattern_hash_val,string_window_hash_val)

    for i in range(1,len(string)-window_size):
        string_window_hash_val -= ht[string[i-1]] * (total_chars ** window_size-1)
        string_window_hash_val *= total_chars
        string_window_hash_val += ht[string[i+window_size-1]]
        if string_window_hash_val == pattern_hash_val:
            count+=1
            indices.append(i)
    
    print('Count---->',count)
    print('Indices-->',indices)

string = 'aabaabaab'
pattern= 'aab'
RabinKarp(string,pattern)