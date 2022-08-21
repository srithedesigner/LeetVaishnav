class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        
        
        ans = []
        
        n = len(stamp)
        m = len(target)
        
        stamp, target = list(stamp), list(target)
        
        done = False
        
        while not done:
            
            done = True
            
            for i in range(m - n + 1):
                
                canStamp = False
                for j in range(n):
                    
                    if target[i + j] == "?":
                        continue
                        
                    if target[i+j] != stamp[j]:
                        canStamp = False
                        break
                    
                    canStamp = True
                
                if canStamp:
                    
                    for j in range(n):
                        
                        target[i+j] = "?"
                    
                    ans.append(i)
                    
                    done = False
        
        return [] if target != ["?"]*m else ans[::-1]
        
        