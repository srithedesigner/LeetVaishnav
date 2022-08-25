class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        
        mod = 10**9 + 7
        
        @lru_cache(None)
        def position(pos, steps):
            
            if steps == 0:
                
                if pos == 0:
                    return 1
                return 0
            
            ans = 0
            
            #left :
            
            if pos > 0:
                
                ans += position(pos - 1, steps - 1)
            #right:
            
            if pos < arrLen - 1:
                ans += position(pos + 1, steps - 1)
            
            #stay
            
            ans += position(pos, steps - 1)
            
            return ans%mod
        
        return position(0, steps)