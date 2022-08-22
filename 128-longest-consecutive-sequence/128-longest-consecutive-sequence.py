class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ans = 0 
        
        l = set(nums)
        
        for i in l:
            
            if i-1 not in l:
                
                a = 1
                n = i;
                
                while(n+1 in l):
                    a+=1;
                    n = n+1
                ans = max(ans,a)
        
        return ans
        