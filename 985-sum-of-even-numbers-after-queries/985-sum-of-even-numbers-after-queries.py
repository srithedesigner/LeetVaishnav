class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        evenSum = sum(list(filter(lambda x : x%2 == 0, nums)))
        ans = [0] * len(queries)
        
        for index, (val, ind) in enumerate(queries):
            
            if (val + nums[ind])%2 == 0:
                
                if nums[ind]%2 == 0:
                    
                    evenSum += val
                else:
                    evenSum += (nums[ind] + val)
            else:
                
                if nums[ind]%2 == 0:
                    evenSum -= nums[ind]
            
            nums[ind] += val
            ans[index] = evenSum
        
        return ans
        