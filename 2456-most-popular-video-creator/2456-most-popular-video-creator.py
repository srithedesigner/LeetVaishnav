class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        
        cv = list(zip(creators, views))
        
        func = lambda x : x[0]
        cv.sort(key = func)
        
        pop = []
        for key, group in groupby(cv, lambda x: x[0]):
            s = 0
            for k, val in list(group):
                s += val
            pop.append((k, s))
        
        pop.sort(key = lambda x: -x[1])
        
        mx = pop[0][1]
        
        #print(pop)
        
        ans = []
        for key, group in groupby(sorted(zip(creators, ids, views)), lambda x: x[0]):
            s = 0
            m = 0
            mid = "~"
            for k, i, v in list(group):
                s += v
                
                if v == m:
                    mid = min(mid, i)
                    
                if v > m:
                    m = v
                    mid = i

            
            if s == mx:
                ans.append([key, mid])
        return ans