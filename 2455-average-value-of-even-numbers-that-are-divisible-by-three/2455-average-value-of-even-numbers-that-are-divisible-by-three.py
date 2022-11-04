class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        
        n = 0
        s = 0
        
        for num in nums:
            if num%6 == 0:
                s += num
                n += 1
        if n == 0:
            return 0
        return s//n