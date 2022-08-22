class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        
        LIS = [0] * 26
        
        ans = 1
        for c in s:
            
            ind = ord(c) - ord('a')
            mx = -1
            
            for i in range(-k, k+1):
                
                if 0 <= ind+i < 26:
                    
                    mx = max(mx, LIS[ind + i])
                
            LIS[ind] = mx + 1
                    
                    
            ans = max(ans, LIS[ind])
            
    
        
        return ans
                
        
        