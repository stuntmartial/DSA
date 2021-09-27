class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_len=float('inf')
        start_index=0
        ptr=0
        curr_sum=0
        curr_len=0
        
        while ptr<len(nums):
            curr_sum+=nums[ptr]
            curr_len+=1
            #min_len=min(min_len,curr_len)
            
            if curr_sum<target:
                ptr+=1
                
            elif curr_sum>=target:
                while curr_sum>=target:
                    
                    print('si: ',start_index)
                    print('len: ',curr_len)
                    if curr_sum>=target:
                        min_len=min(min_len,curr_len)
                    curr_sum-=nums[start_index]
                    start_index+=1
                    curr_len-=1
                    
                
                ptr+=1
                
                
        print(min_len)
        if min_len==float('inf'):
            min_len=0
        return min_len