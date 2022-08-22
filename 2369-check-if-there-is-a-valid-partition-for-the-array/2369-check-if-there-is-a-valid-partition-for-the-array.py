class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        @lru_cache(None)
        def recursion(x):
            
            #print(x)
            if x == 0:
                return False
            
            if x == 1:
                
                if nums[x] == nums[x-1]:
                    return True
                return False
            
            if x == 2:
                
                if nums[x] == nums[x-1] and nums[x] == nums[x-2]:
                    return True
                
                if nums[x] == nums[x-1] + 1 and nums[x-2] == nums[x-1] - 1:
                    return True
                
                return False
            
            
            ans = False
            
            
            
            if nums[x] == nums[x-1]:
                ans |= recursion(x-2)
            
            if nums[x] == nums[x-1] and nums[x] == nums[x-2]:
                ans |= recursion(x-3)
            
            if (nums[x] == nums[x-1] + 1) and (nums[x-2] == nums[x-1] -1):
                #print('hi')
                ans |= recursion(x-3)
            
            return ans
        
        return recursion(n-1)
                