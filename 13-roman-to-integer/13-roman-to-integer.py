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
        
        
        order = [
                    "I",
                    "V",
                    "X",
                    "L",
                    "C",
                    "D",
                    "M",
                ]
        
        order.sort(key = lambda x : d[x])
        
        order_id = {
            
        }
        
        for ind, val in enumerate(order):
            
            order_id[val] = ind
        
        
        x = 0
        
        ans = 0
        
        while x < len(s):
            
            #print(x)
            
            dif = 0
            
            while x < len(s)-1  and order_id[s[x]] < order_id[s[x+1]]:
                
                dif += d[s[x]]
                x+=1
            
            ans += d[s[x]]
            ans -= dif
            
            x += 1
        
        return ans
            
            