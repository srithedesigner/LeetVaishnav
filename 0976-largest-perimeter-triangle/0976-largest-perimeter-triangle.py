class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        for i in range(n-3, -1, -1):
            
            x = nums[i]
            y = nums[i+1]
            z = nums[i+2]
            
            #print(x, y, z)
            
            if x + y > z:
                return x + y + z
        
        return 0