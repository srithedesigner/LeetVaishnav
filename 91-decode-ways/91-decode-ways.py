class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def recursion(ind):
            
            if ind >= len(s):
                return 1
            
            if s[ind] == "0":
                return 0
            
            ans = 0
            
            ans += recursion(ind + 1)
            
            if ind < len(s)-1:
                
                if 1 <= int(s[ind:ind+2]) <= 26:
                    ans += recursion(ind + 2)
            
            return ans
        
        return recursion(0)
                    
            
                            