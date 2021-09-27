class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht={}
        for i in s:
            try:
                ht[i]+=1
            except:
                ht[i]=1
                
        for i in t:
            try:
                ht[i]-=1
                if ht[i]<0:
                    return False
            except:
                return False
            
        for i in ht.keys():
            if ht[i]!=0:
                return False
            
        return True