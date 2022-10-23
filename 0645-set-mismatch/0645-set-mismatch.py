class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        a_b = 0
        
        for ind, val in enumerate(nums):
            
            a_b ^= val
            a_b ^= (ind+1)
        
        for ind, val in enumerate(nums):
            
            val = abs(val)
            
            nums[val-1] = -1 * abs(nums[val - 1])
        
        #print(*nums)
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return [a_b ^ (i+1), i+1]
        
        #return []