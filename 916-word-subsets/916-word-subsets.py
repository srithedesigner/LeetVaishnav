class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        chars = defaultdict(int)
        
        for i in words2:
            
            d = defaultdict(int)
            for j in i:
                d[j] += 1
            
            
            for j in d:
                chars[j] = max(chars[j], d[j])
        
        ans = []
        
        for i in words1:
            
            c = defaultdict(int)
            for j in i:
                c[j] += 1
            
        
            for x in chars:
                
                if c[x] < chars[x]:
                    break
                
            else:
                ans.append(i)
                                    
        
        return ans