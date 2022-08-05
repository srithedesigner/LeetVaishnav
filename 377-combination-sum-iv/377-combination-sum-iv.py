class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        @lru_cache(None)
        def recursion(x, target):
            
            if x == len(nums):
                return 0
            
            if target == 0:
                return 1
            
            if target < 0:
                return 0
            
            
            return recursion(0, target - nums[x]) + recursion(x + 1, target)
        
        return recursion(0, target)
    
    
            