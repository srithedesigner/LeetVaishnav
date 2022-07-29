class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def getOrder(s):
            
            s = s + "#"
            
            d = {}
            x = 0
            for i in s:
                if i not in d:
                    d[i] = str(x)
                    x+=1
                    
            ok = []
            c = 1
            prev = s[0]
            for i in range(1, len(s)):
                
                if s[i] == prev:
                    c += 1
                else:
                    ok.append("_" + d[s[i]] + "*" + str(c))
                    c = 1
                    prev = s[i]
            
                
                
            
            return "".join(ok)
                
            
            
        #print(getOrder("xyx"))
        
        p = getOrder(pattern)
        
        ans = []
        
        for i in words:
            if getOrder(i) == p:
                ans.append(i)
        
        return ans