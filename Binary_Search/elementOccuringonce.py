class Solution:
    def singleNonDuplicate(self, arr):
        
        
        if len(arr)==1:
            return arr[0]
        
        low = 0;high = len(arr)-1
        
        while low<=high:
            mid = low + (high-low)//2
            
            #Checking corners 0 and last
            if mid==0:
                if arr[mid+1]!=arr[mid]:
                    return arr[mid]
                else:
                    break
            
            if mid==len(arr)-1:
                if arr[mid-1]!=arr[mid]:
                    return arr[mid]
                else:
                    break
            
            #Checking middle both shd be true....neither present in left nor in right
            # if 1,1,2, 3 ,3,4
            #          ...
            #if OR is used left is satisfied but right is not , so shd this be answer ---> NOOO
            # thats why separate edge cases check 
            if (mid-1>=0 and arr[mid-1]!=arr[mid]) and (mid+1<len(arr) and arr[mid+1]!=arr[mid]):
                return arr[mid]
            
            
            #Encountered position is first or second.......can be done in either ways!!!!!
            if mid-1>=0 and arr[mid-1]==arr[mid]:#SecondOcc
                if (mid-1)%2==0:
                    low=mid+1
                else:
                    high=mid-1
            
            elif mid+1<len(arr) and arr[mid+1]==arr[mid]:#firstOcc
                if mid%2==0:
                    low=mid+1
                else:
                    high=mid-1
                    
        return -1