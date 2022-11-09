class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        
        for ind, val in enumerate(secret):
            
            if val == guess[ind]:
                bulls += 1
        
        cS = Counter(secret)
        cG = Counter(guess)
        
        cows = 0
        
        for x in cG:
            if x in cS:
                cows += min(cG[x], cS[x])
        
        return f"{bulls}A{cows - bulls}B"
    
    