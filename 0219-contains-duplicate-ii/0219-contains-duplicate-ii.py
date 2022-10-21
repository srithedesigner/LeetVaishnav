class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        s = set()
        k+=1
        
        if len(nums) <= k:
            for i in nums:
                if i in s:
                    return True
                s.add(i)
            return False
        
        for i in range(k):
            if nums[i] in s:
                return True
            s.add(nums[i])
        
        for i in range(k, len(nums)):
            s.remove(nums[i-k])
            
            if nums[i] in s:
                return True
            s.add(nums[i])
    
        return False