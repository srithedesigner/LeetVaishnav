class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        se = Counter(s)
        
        ans = -1
        
        for i in range(len(s)-1, -1, -1):
            
            if se[s[i]] == 1:
                ans = i
                
                
                
        
        return ans