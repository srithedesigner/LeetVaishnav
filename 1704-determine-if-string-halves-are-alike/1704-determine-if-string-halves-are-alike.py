class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        n = len(s)
        
        vowels = {"a", "e", "i", "o", "u"}
        
        x = 0
        
        for i in s[:n//2]:
            if i.lower() in vowels:
                x += 1
        
        for i in s[n//2:]:
            if i.lower() in vowels:
                x -= 1
        
        return x == 0