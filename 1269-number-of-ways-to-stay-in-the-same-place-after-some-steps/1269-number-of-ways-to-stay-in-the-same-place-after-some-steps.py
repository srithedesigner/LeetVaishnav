class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        arrLen = min(arrLen, steps//2 + 2)
        
        mod = 10**9 + 7
        
        dp = [0 for i in range(arrLen)]
        buf = [0 for i in range(arrLen)]
        
        dp[0] = 1
        
        for i in range(1, steps+1):
            
            
            
            for j in range(0, arrLen):
                
                x = 0
                x += (dp[j]%mod)
                
                if j-1 >= 0:
                    
                    x += (dp[j-1]%mod)
                
                if j + 1 < arrLen:
                    x += (dp[j+1]%mod)
                    
                x %= mod
                
                buf[j] = x
            
            for c in range(len(buf)):
                dp[c] = buf[c]
                
        
        
        return dp[0]
            
            
            
        
        
        