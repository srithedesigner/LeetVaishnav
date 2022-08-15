class Solution:
    def romanToInt(self, s: str) -> int:
        
        d = {
                "I"      :       1,
                "V"      :       5,
                "X"      :       10,
                "L"      :       50,
                "C"      :       100,
                "D"      :       500,
                "M"      :       1000,
            }
        
        
        
        
        x = 0
        
        ans = 0
        
        while x < len(s):
            dif = 0
            
            while x < len(s)-1  and d[s[x]] < d[s[x+1]]:
                
                dif += d[s[x]]
                x+=1
            
            ans += d[s[x]]
            ans -= dif
            
            x += 1
        
        return ans
            
            