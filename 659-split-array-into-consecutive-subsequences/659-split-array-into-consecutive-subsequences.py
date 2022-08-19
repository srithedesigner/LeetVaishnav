class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        c = Counter(nums)
        
        print(c)
        tails = defaultdict(lambda : 0)
        
        nums = sorted(list(set(nums)))
        #print(nums)
        for x in nums:
            
            if tails[x-1] + min(c[x+1], c[x+2]) < c[x]:
                
                 
                #print(x)
                return False
            
            if c[x] <= 0:
                continue
            
            
            fwd = min(c[x+1], c[x+2])
            
            back = tails[x-1]
            
            p = c[x]
            
            if p <= back:
                
                tails[x-1] -= p
                tails[x] += p
                
            else:
                
                 
                tails[x] += tails[x-1]
                
                c[x+1] -= (c[x] - tails[x-1])
                c[x+2] -= (c[x] - tails[x-1])
                
                
               
                tails[x+2] += (c[x] - tails[x-1])
                
                tails[x-1] = 0
                
        
        #print(tails)
               
        
        return True
                
                
                
                
                