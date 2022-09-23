class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        ans = 0
        MOD = 1000000000 + 7
        
        for i in range(1, n+1):
            
            x = int(math.log(i, 2))
            ans = ans << (x+1)
            ans += i
            ans = ans%MOD
        
        return ans