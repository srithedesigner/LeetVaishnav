class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        
        c = Counter(arr)
        
        s = list(set(arr))
        
        ans = 0
        
        s.sort(key = lambda x : -c[x])
        #print(s)
        p = len(arr)
        i = 0
        
        while p > len(arr)//2:
            
            p -= c[s[i]]
            #print(arr[i])
            i+=1
            
        
        return i
            
        