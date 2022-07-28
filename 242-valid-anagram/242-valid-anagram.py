class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(list(s))
        d = Counter(list(t))
        
        for i in c:
            if i not in d:
                return False
            
            if c[i] != d[i]:
                return False
        
        for i in d:
            if i not in c:
                return False
            
            if c[i] != d[i]:
                return False
        
        return True
                