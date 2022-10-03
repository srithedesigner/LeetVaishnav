class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        x = list(zip(colors, neededTime))
        ans = 0
        
        for key, group in groupby(x, lambda x : x[0]):
            
            ans += max(list(group))[1]
        
        return sum(neededTime) - ans