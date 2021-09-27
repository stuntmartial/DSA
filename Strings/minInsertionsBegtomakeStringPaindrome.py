class Solution:
    
    def getLPS(self,s):
        if len(s)==1:
            return [0]
        
        LPS=[0]*len(s)
        rp=0;i=1
        
        while i<len(s):
            if s[i]==s[rp]:
                LPS[i]=rp+1
                rp+=1
                i+=1
            else:
                if rp>0:
                    rp=LPS[rp-1]
                else:
                    LPS[i]=0
                    i+=1  
        return LPS
        
    def reverse(self,s):
        if s=="":
            return ""
        revStr=""
        for i in range(len(s)-1,-1,-1):
            revStr+=s[i]
        return revStr
    
    def shortestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        
        #Target ----> maximum palindrome prefix .... so we can insert the next chars
        #in reverse order in the begining
        # s=abbaklm    "abba"klm # mlk"abba"
        # LPS gives how much of prefix matches suffix
        # reverse string and add it with a # in between
        # if any palindromix prefix is present then reversing and adding with generate the same sequence of chars 
        # at the end, so just use lps

        trgtStr=s+"#"+self.reverse(s)
        LPS=self.getLPS(trgtStr)
        insertionCount=len(s)-LPS[-1]
        
        if insertionCount==0:
            return s
        else:
            insertionStr=""
            for ch in s[LPS[-1]:]:
                insertionStr=ch+insertionStr
            return insertionStr+s