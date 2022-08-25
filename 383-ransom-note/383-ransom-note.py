class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        r = Counter(ransomNote)
        m = Counter(magazine)
        
        for i in r:
            if i not in m or m[i] < r[i]:
                return False
        return True