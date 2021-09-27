class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        if len(nums)==1:
            if nums[0]==k:
                return 1
            else:
                return 0
            
        cum_sum=0 #nums[0]
        count=0
        sum_hash={}
        print(cum_sum,sum_hash)
        for i in range(0,len(nums)):#1
            cum_sum=cum_sum+nums[i]
            
            if cum_sum==k:
                count+=1
            
            try:
                count+=sum_hash[cum_sum-k]
            except:
                pass
            
            try:
                sum_hash[cum_sum]+=1
            except:
                sum_hash[cum_sum]=1
            
            
        return count
arr=[-1,-1,1]
target=0
func(arr,len(arr),target)