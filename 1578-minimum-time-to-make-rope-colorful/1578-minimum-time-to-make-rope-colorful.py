class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        return sum(neededTime) - sum([max(list(group))[1] for key, group in groupby(list(zip(colors, neededTime)), lambda x : x[0])])