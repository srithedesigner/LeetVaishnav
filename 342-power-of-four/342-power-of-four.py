class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        
        t_zeros = 0
        
        if( n&(n-1)) != 0:
            return False
        
        while n:
            
            n = (n >> 1)
            t_zeros += 1
        #print(t_zeros)
        if t_zeros%2 == 1:
            return True
        
        return False