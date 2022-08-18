class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        
        c = Counter(arr)
        
        s = list(set(arr))
        
        
        d = defaultdict(int)
        
        for i in c:
            
            d[c[i]] += 1
    
        
        i = len(arr)
        x = 0
        p = len(arr)
        #print(d)
        while p > len(arr)// 2 and  i >= 0:
            
            
            if i in d:
                
                while p > len(arr)//2 and d[i] > 0:
                    p -= i

           
                    x += 1
                    d[i]-=1
            i-=1 
        return x
            
            
            
        