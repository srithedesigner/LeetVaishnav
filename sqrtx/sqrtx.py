class Solution:
    def mySqrt(self, x: int) -> int:
        
        low = 0
        high = x
        
        ans = 0
        
        while low <= high:
            
            

            mid = low + (high - low)//2
            #print(mid)
            
            if mid**2 == x:
                return mid
            
            if mid**2 > x:
                high = mid - 1
            
            else:
                ans = max(ans, mid)
                low = mid + 1
                
                
        return ans