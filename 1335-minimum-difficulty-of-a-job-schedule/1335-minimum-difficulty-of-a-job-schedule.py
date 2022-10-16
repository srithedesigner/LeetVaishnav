class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @lru_cache(None)
        def recursion(ind: int, days: int):
            
            if ind >= len(jobDifficulty):
                if days != 0:
                    return float('inf')
                return 0
            
            if days < 0:
                return float('inf')
            if days == 0:
                return max(jobDifficulty[ind:])
            m = 0
            ans = float('inf')
            for i in range(ind, len(jobDifficulty)):
                
                m = max(m, jobDifficulty[i])
                
                ans = min(ans, m + recursion(i + 1, days - 1))
            return ans
        ret = recursion(0, d)
        return ret if ret!= float('inf') else -1