class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        def digitSum(x):
            s = 0
            for i in str(x):
                s += int(i)
            return s
        
        ans = 0
        
        x = n
        mult = 10
        
        
        while digitSum(x) > target:
        
            pos = mult - x%mult
            
            x += pos
            ans += pos
            
            mult *= 10
    
        return ans
            