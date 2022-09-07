from sortedcontainers import SortedList

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(list)
        
        for ind, val in enumerate(parent):
            
            if val != -1:
                
                graph[val].append(ind)
                
        
        
        max_len = defaultdict(lambda : 1)
        
        def get_max_len(node):
            
            
            max_d = 1
            
            for i in graph[node]:
                x = get_max_len(i)
                if s[i] != s[node]:
                    
                    max_d = max(max_d, x + 1)
                
                
            max_len[node] = max_d
            
            return max_d
        
        get_max_len(0)
        
        #print(max_len)
        
        #@lru_cache(None)
        def get_longest_path(node):
            
            long = 1
            
            ok = SortedList()
            
            for child in graph[node]:
                
                if s[child] != s[node]:
                    
                    ok.add(max_len[child])
                    
                 
            
            if len(ok) == 0:
                return long
            
            if len(ok) == 1:
                
                return ok[0] + 1
            
            return ok[-1] + ok[-2] + 1
                
            
        return max([get_longest_path(x) for x in range(len(parent))])
                
                
                