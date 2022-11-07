class Solution:
    def maximum69Number (self, num: int) -> int:
        
        mult = 1000
        
        while mult > 0:
            
            if (num//mult)%10 == 6:
                
                return num + 3 * mult
            
            mult //= 10
        
        
        return num