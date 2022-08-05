class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        dp = defaultdict(lambda : 1)
        
        for i in range(1, target + 1):
            dp[i] = sum([dp[i - num] for num in nums if num <= i])
        
        return dp[target]
    
    
            