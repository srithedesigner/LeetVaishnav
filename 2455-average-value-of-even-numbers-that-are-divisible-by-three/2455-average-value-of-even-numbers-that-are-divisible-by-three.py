class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        
        nums = [x for x in nums if not x%6]
        
        return sum(nums)//len(nums) if nums else 0