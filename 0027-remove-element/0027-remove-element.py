class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        ans = len(nums) - nums.count(val)
        
        while left < right:
            
            while left < right and nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            
            left += 1
        
        return ans
    
    