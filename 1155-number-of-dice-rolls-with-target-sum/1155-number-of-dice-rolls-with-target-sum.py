class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        mod = 1000000000+7
        
        @lru_cache(None)
        def recursion(i, target):
            #print(i)
            if i >= n:
                #print("hi")
                if target == 0:
                    return 1
                return 0
            
            ans = 0
            for x in range(1, k+1):
                
                if x <= target:
                    ans += recursion(i+1, target - x)%mod
                    ans%=mod
            
            return ans
        
        return recursion(0, target)%mod
                
            
            