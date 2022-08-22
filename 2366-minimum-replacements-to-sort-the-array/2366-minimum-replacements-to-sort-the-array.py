class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        prev = float('inf')
        
        ans = 0
        
        for i in range(len(nums)-1, -1, -1):
            
            if nums[i] <= prev:
                prev = nums[i]
                continue
            
            
            count = ceil(nums[i]/ prev)
            
            ans += (count - 1)
            
            prev = nums[i] // count
        
        return ans