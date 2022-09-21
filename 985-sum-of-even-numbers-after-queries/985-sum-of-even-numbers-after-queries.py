class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        evenSum = sum(list(filter(lambda x : x%2 == 0, nums)))
        ans = []
        
        for val, ind in queries:
            
            if nums[ind]%2 == 0:
                evenSum -= nums[ind]
            
            nums[ind] += val
            
            if nums[ind]%2 == 0:
                evenSum += nums[ind]
            
            ans.append(evenSum)
        
        return ans
            
    