class Solution:
    def maximizeXor(self, nums: List[int], q: List[List[int]]) -> List[int]:
        
        if len(q) == 1:
            
            ans = 0
            
            for i in nums:
                if i <= q[0][1]:
                    ans = max(ans, i^q[0][0])
            
            return [ans]
                    
        
        
        class Trie:
            
            def __init__(self):
                self.zero = None
                self.one = None
        
        trie = Trie()
        
        
        def add_number(num):
            
             
            
            curr = trie
            
            for i in range(31, -1, -1):
                
                if (num & (1 << i)) != 0:
                    
                    if curr.one == None:
                        curr.one = Trie()
                        
                    
                    curr = curr.one
                    
                
                else:
                    
                    if curr.zero == None:
                        curr.zero = Trie()
                    
                    curr = curr.zero
            
                    
                    
        
        
        def find_max(num):
            
            curr = trie
            
            ans = 0
            
            for i in range(31, -1, -1):
                
                if (num & (1 << i)) != 0:
                    
                    if curr.zero != None:
                        curr = curr.zero
                        ans += (1 << i)
                    else:
                        curr = curr.one
                
                else:
                    
                    if curr.one != None:
                        curr = curr.one
                        ans += (1 << i)
                    else:
                        curr = curr.zero

            
            return ans
                
                
        
        
        queries = sorted(q, key = lambda x : x[1])
        nums.sort()
        
        ans = {}
        
        x = 0
        
        for num, limit in queries:
            
            if x == 0 and nums[x] > limit:
                ans[(num, limit)] = -1
                continue
            
            while x < len(nums) and nums[x] <= limit:
                add_number(nums[x])
                x += 1
            
            ans[(num, limit)] = find_max(num)
        
        
        ret = []
        for num, limit in q:
            ret.append(ans[(num, limit)])
        
        return ret
                
        
        