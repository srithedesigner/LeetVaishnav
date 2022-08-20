class Solution:
    def minRefuelStops(self, target: int, startFuel: int, st: List[List[int]]) -> int:
        
        
        heap = []
        
        curr = startFuel
        
        i = 0
        
        ans = 0
        
        if curr >= target:
            return 0
        
        while curr < target:
            
            
            while i < len(st) and curr >= st[i][0]:
                heapq.heappush(heap, -st[i][1])
                i+=1
                
            
            if curr >= target:
                return ans
            
            if len(heap) == 0:
                return -1
            
            pt = -heapq.heappop(heap)
            
            ans += 1
            
            curr += pt
            
            
             
        
        return ans
                
                
            
            
            