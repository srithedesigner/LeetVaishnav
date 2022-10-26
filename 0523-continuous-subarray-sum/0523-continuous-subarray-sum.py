
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixes =  {}
        
        prefixes[0] = -1
        
        prefix = 0

        for ind, val in enumerate(nums):
            prefix = (prefix + val) % k
            
            if prefix in prefixes:
                i = prefixes[prefix]
                if ind - i >= 2:
                    return True

            if prefix not in prefixes:
                prefixes[prefix] = ind
        
        
        return False
    