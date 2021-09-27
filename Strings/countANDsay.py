class Solution:
    def countAndSay(self, n: int) -> str:
        if n==0:
            return ""
        elif n==1:
            return "1"
        elif n==2:
            return  "11"
        
        num="11$"
        
        for i in range(3,n+1):
            ptr=1;count=1;new_num=""
            
            while ptr<len(num):
                print('ptr at ',num[ptr])
                if num[ptr]==num[ptr-1]:
                    count+=1
                else:
                    new_num=new_num+str(count)+num[ptr-1]
                    count=1
            
                ptr+=1
                
            num=new_num+'$'
            print(new_num)
        
        if num[len(num)-1]=='$':
            return num[0:len(num)-1]
        return num