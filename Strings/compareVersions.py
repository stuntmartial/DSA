class Solution:
    
    def removePrecedingZeros(self,s):
        for i in s:
            if i=="0":
                if len(s)==1:
                    return s
                s=s[1:]
            else:
                return s        
        
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = [i for i in version1.split(".")]
        l2 = [i for i in version2.split(".")]
        print(l1,l2)
        if len(l1)>len(l2):
            for i in range(len(l1)-len(l2)):
                l2.append("0")
        elif len(l2)>len(l1):
            for i in range(len(l2)-len(l1)):
                l1.append("0")
                
        for i in range(len(l1)):
            rev1 = l1[i]
            rev2 = l2[i]
            
            rev1 = self.removePrecedingZeros(rev1)
            rev2 = self.removePrecedingZeros(rev2)
            print(rev1,rev2)
            if int(rev1)>int(rev2):
                return 1
            elif int(rev1)<int(rev2):
                return -1
            
        return 0