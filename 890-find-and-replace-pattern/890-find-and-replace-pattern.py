class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        patt = set()
        order = []
        for i in pattern:
            if i not in patt:
                order.append(i)
                patt.add(i)
        
        def match(x):
            
            
            if len(set(x)) != len(order):
                return False
            
            p = 0
            
            d = {}
            
            for i in x:
                if i not in d:
                    d[i] = order[p]
                    p+=1
            
            changed = []
            
            for i in x:
                changed.append(d[i])
                
            return "".join(changed) == pattern
        
        
        
        return list(filter(match, words))
                    
        