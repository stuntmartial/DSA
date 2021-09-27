class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = list()
        ht = dict()
        null_key = self.generate_null_key()
        for i in strs:
            if i=="":
                try:
                    ht[null_key].append(i)
                except:
                    ht[null_key]=[i]
                    
            else:
                count_key=self.generate_key(i)
                print(count_key)
                try:
                    ht[count_key].append(i)
                except:
                    ht[count_key]=[i]
                    
        for i in ht.keys():
            op.append(ht[i])
            
        return op
            
    def generate_null_key(self):
        null_key=''
        for i in range(26):
            null_key=null_key+'0'
            
        return null_key
    
    def generate_key(self,string):
        print(string)
        l = [0]*26
        for i in string:
            print('i-->',i,ord(i)-97)
            l[ord(i)-97] += 1
            print(l)
            
        count_key=''
        for i in l:
            count_key = count_key+"#"+str(i)
            
        print(count_key)
        return count_key