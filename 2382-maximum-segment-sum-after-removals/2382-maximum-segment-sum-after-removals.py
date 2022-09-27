class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        
        n = len(nums)
        parent = [-1 for i in range(n)]
        s = [nums[i] for i in range(n)]
        
        rank = [1 for i in range(n)]
        
        def find(x):
            
            if parent[x] == -1:
                parent[x] = x
            
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        
        def union(x, y):
            
            x, y = find(x), find(y)
            
            if rank[y] > rank[x]:
                x, y = y, x
            
            parent[y] = x
            s[x] += s[y]
            rank[x] += rank[y]
        
        ret = []
        
        ans = 0
        for ind in range(n-1, -1, -1):
            
            ret.append(ans)
            
            i = removeQueries[ind]
            
            if i < n-1 and parent[i+1] != -1:
                union(i, i+1)
            
            if i > 0 and parent[i-1] != -1:
                union(i, i-1)
            
            ans = max(ans, s[find(i)])
            
        return ret[::-1]        