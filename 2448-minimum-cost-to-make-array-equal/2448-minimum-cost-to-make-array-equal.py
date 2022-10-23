class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        low = 0
        high = max(nums) + 1
        
        def calculate(x):
            
            ans = 0
            for ind, val in enumerate(nums):
                ans += (abs(x - val) * cost[ind])
            
            return ans
        
        ans = float('inf')
        
        while low + 2 < high:
            
            m1 = low + (high - low)//3
            m2 = high - (high - low)//3
            
            f1, f2 = calculate(m1), calculate(m2)
            
            ans = min(ans, min(f1, f2))
            
            if f1 > f2:
                low = m1
            
            else:
                high = m2
            
        
        for i in range(low , high + 1):
            ans = min(ans, calculate(i))
        
        return ans