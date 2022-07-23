from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0 for i in range(n)]
        
        sList = SortedList()
        
        for i in range(n-1, -1, -1):
            
            ans[i] = sList.bisect_left(nums[i])
            sList.add(nums[i])
            
        
        return ans