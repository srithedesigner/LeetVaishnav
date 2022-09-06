class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        wordDict = set(wordDict)
        
        @lru_cache(None)
        def recur(i):
            
            #print(i)
            
            if i == len(s):
                return True
            
            w = []
            
            ok = False
            
            for x in range(i, len(s)):
                
                w.append(s[x])
                
                if "".join(w) in wordDict:
                    
                    #print("hi", "".join(w))
                    
                    ok = ok | recur(x+1)
            
            return ok
        
        return recur(0)
                    
                    
            
            