class Solution:
    def nextPermutation(self, nums):
        
        n=len(nums)
        ind1=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind1=i
                break
                
        print('ind1--->',ind1)
        if ind1==-1:
            print('hhhhh')
            nums.reverse()
            return
        
        ind2=-1
        for i in range(n-1,ind1,-1):
            if nums[i]>nums[ind1]:
                ind2=i
                break
                
        print(ind1,ind2)
        nums[ind1],nums[ind2]=nums[ind2],nums[ind1]
        print(arr)
        rev(nums,ind1+1,len(nums))
        
def rev(arr,start,end):
    print('Entering reverse')
    j=0
    for i in range(start,end):
        print(i,end-j-1)
        arr[i],arr[end-1-j]=arr[end-1-j],arr[i]
        j+=1
        if j==((end-1-start)//2)+1:
            break
        
arr=[1,2,3]
print(arr)
Solution().nextPermutation(arr)
print(arr)