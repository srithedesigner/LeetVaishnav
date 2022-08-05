class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        dp = defaultdict(int)
        dp[0] = 1
        
        for i in range(target + 1):
            
            for x in nums:
                
                if x <= i:
                    
                    dp[i] += dp[i - x]
        
        return dp[target]
    
    
            