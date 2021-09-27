class Solution:
    def minWindow(self,s,t):        
        
        if len(s)<len(t):
            return ""

        print('s_length : ',len(s))
        
        fixed_hash = {i:0 for i in s}
        window_hash = {i:0 for i in s}
        for i in t:
            fixed_hash[i] = 0
            window_hash[i] = 0

        
        for i in t:
            fixed_hash[i]+=1
            
        print(fixed_hash)
        print()
        print()
        min_substr=''
        substr=''
        min_len=float('inf')
        desired_count=sum([fixed_hash[i] for i in fixed_hash.keys()])
        curr_count=0
        curr_len=0
        ptr1=0;ptr2=-1
        
        while ptr2<len(s):
            print('substr received : ',substr)
            if curr_count<desired_count:
                ptr2+=1
                if ptr2==len(s):
                    break
                print('Now ptr2>>>>',ptr2)
                substr+=s[ptr2]
                
                window_hash[s[ptr2]]+=1
                
                if window_hash[s[ptr2]]<=fixed_hash[s[ptr2]]:
                    curr_count+=1
                curr_len+=1
                
            elif curr_count==desired_count:
                print('MATCHED>>>>>>>',ptr1,ptr2)
                print('window_hash:',window_hash)
                if curr_len<min_len:
                    min_substr=substr
                    min_len=curr_len
                    
                popped_char=substr[0]
                substr=substr.replace(popped_char,'',1)
                ptr1+=1

                
                if window_hash[popped_char]==fixed_hash[popped_char]:
                    curr_count-=1
                    
                curr_len-=1
                window_hash[popped_char]-=1

                print('ptr1>>>',ptr1,'ptr2>>>>',ptr2)
                print('curr_len : ',curr_len)
                print('window_hash: ',window_hash)
                    
        print('op>>>>>',min_substr)
        return min_substr
    
  
S=Solution()
s='a'
t='b'
print(s,t)
S.minWindow(s,t)