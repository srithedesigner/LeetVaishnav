class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        s = sum(nums)
        
        diff = float('inf')
        
        n = len(nums)
        curr = 0
        ans = 0
        for ind, val in enumerate(nums[:-1]):
            curr += val
            s -= val
            
            curr_dif = abs(curr//(ind + 1) - (s//(n-ind-1)))
            
            if curr_dif < diff:
                diff = curr_dif
                ans = ind
        if sum(nums)//n < diff:
            ans = n - 1
        return ans
                
            