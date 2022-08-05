class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        
        zero = bisect.bisect_left(nums, 0)
        
        if zero == 0:
            return list(map(lambda x : x*x , nums))
        
        if zero == n:
            
            return list(map(lambda x : x*x , nums))[::-1]
        
        i = zero
        j = zero - 1
        
        ans = []
        
        while j >=0 and i < n:
            
            if nums[i] < -nums[j]:
                ans.append(nums[i]**2)
                i+=1
            
            else:
                ans.append(nums[j]**2)
                j-=1
        
        while j >= 0:
            ans.append(nums[j]**2)
            j-=1
                
        while i < n:
            ans.append(nums[i]**2)
            i+=1
        
        return ans
            
            
            
            
        