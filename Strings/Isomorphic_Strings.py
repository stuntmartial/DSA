class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        ht1={}
        ht2={i:True for i in t}
        for i in range(len(s)):
            try:
                if ht1[s[i]] != t[i] :
                    return False
            except:
                if ht2[t[i]] == False:
                    return False
                ht1[s[i]] = t[i]
                ht2[t[i]] = False
                
                
        return True