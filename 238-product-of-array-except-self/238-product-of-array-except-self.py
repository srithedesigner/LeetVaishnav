class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
         
        suffix = [None]*len(nums)
        
        suffix[-1] = nums[-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
            
        
        prefix = 1
        
        ans = []
        
        for i in range(n-1):
            
            ans.append(prefix * suffix[i+1])
            prefix *= nums[i]
        
        ans.append(prefix)
        
        return ans