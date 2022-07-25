class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        x, y = bisect_left(nums, target), bisect_right(nums, target)
        
        print(x, y)
        ans = []
        
        if x < len(nums) and nums[x] == target:
            ans.append(x)
        else:
            ans.append(-1)
            
        
        if 1<= y <= len(nums) and nums[y-1] == target:
            ans.append(y-1)
        elif x< len(nums) and nums[x] == target:
            ans.append(x)
        else:
            ans.append(-1)
            
        
            
        return ans