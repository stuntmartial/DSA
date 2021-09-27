class Solution:
    
    def removePrecedingSpaces(self,s):
        for i in s:
            if i==" ":
                if len(s)==1: #we cannot do s=s[1:] if len(s)=1..so just del it & return ""
                    return ""
                s=s[1:]
            else:
                return s
        return s
    
    def removePrecedingZeros(self,s):
        for i in s:
            if i=="0":
                if len(s)==1:
                    return ""
                s=s[1:]
            else:
                return s
        return s
    
    def convert_to_integer(self,s,negFlag=False):
        num = 0
        for i in range(len(s)):
            #instead of using int(s[i]) below we could create a digits dict {"1":1,"2":2,...}
            #and then use it cuz , we are told to implement atoi but, although not very significant
            #we are still using atoi so better use the digits dict
            num = num*10 + int(s[i])
        if negFlag:
            num*=-1
        return num
    
    def chkLimit(self,num):
        lowerLim = -2**31
        upperLim = (2**31)-1
        
        if lowerLim<=num and num<=upperLim:
            return num
        elif num<lowerLim:
            return lowerLim
        elif num>upperLim:
            return upperLim
        
    def myAtoi(self, s: str) -> int:
        
        digits = [
            str(i) for i in range(0,10)
        ]
        
        negFlag=False
        
        s = self.removePrecedingSpaces(s)
    
        if s=="":
            return 0
        
        if s[0] not in digits and s[0]!="-" and s[0]!="+":
            return 0    
        
        if s[0]=="-":
            negFlag=True
            if len(s)==1:
                return 0
            s=s[1:]
            
        elif s[0]=="+":
            print(s)
            if len(s)==1:
                return 0
            s=s[1:]
        
        s = self.removePrecedingZeros(s)
        if s=="":
            return 0
        
        #We could convert to string to number on the go
        #but generating a new string and then converting it to integer increases code readibility
        newS = ""
        for i in range(len(s)):
            if s[i] not in digits:
                break
            
            newS+=s[i]
        
        num=self.convert_to_integer(newS,negFlag)
        num=self.chkLimit(num)
        return num
            
