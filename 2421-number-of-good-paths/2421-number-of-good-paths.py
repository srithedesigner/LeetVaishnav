class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        parent = {}
        
        def find(x):
            
            if x not in parent:
                parent[x] = x
                
            if parent[x] == x:
                return parent[x]
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            
            x, y = find(x), find(y)
            parent[x] = y
            
        
        adj = defaultdict(list)
        
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        
        verts = defaultdict(list)
        
        for ind, val in enumerate(vals):
            verts[val].append(ind)
            
        
        total = 0
        
        for val in sorted(verts.keys()):
            
            for ind in verts[val]:
                
                for v in adj[ind]:
                    
                    if vals[v] <= val:
                        
                        union(ind, v)
            
            
            comps = defaultdict(int)
            
            for ind in verts[val]:
                
                c = find(ind)
                
                comps[c] += 1
            
            total += sum([i*(i+1)//2 for i in comps.values()])
        
        
        

        return total
            
            
            