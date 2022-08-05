class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        d = defaultdict()
        def recursion(x, target):
            
            if target in d:
                return d[target]
            
            if x == len(nums):
                return 0
            
            if target == 0:
                return 1
            
            if target < 0:
                return 0
            
            d[target] = recursion(0, target - nums[x]) + recursion(x + 1, target)
            
            return d[target]
        
        return recursion(0, target)
    
    
            