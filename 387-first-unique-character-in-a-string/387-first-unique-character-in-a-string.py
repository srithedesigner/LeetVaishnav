class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        se = Counter(s)
        
        
        
        for ind, bal in enumerate(s):
            
            if se[bal] == 1:
                return ind
                
        return -1