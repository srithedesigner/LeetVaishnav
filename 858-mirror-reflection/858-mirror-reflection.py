class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        x = 1
        
        while True:
            
            if (x*q)%p == 0:
                
                k = x*q//p
                
                if x%2 == 0 and k%2 == 0:
                    return 2
            
                
                if x%2 == 1 and k%2 == 1:
                    return 1
                
                
                if x%2 == 1 and k%2 == 0:
                    return 0
        
            x += 1
            
            
            
        