class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        
        left = 0
        right = n-1
        ans = [0 for i in range(n)]
        
        x = n - 1
        
        while left <= right:
            
            if abs(nums[left]) > abs(nums[right]):
                ans[x] = nums[left]**2
                left += 1
            else:
                ans[x] = nums[right]**2
                right -= 1
            x -=1
        
        return ans
            
        
        