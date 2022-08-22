class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        
        
        
        maxSum = sum([max(0, x) for x in nums])
        
        absNums = sorted([abs(x) for x in nums])
        
        
        heap = [(-maxSum + absNums[0], 0)]
        ans = maxSum
        
        while k-1:
            
            #print(heap)
            cur, ind = heapq.heappop(heap)
            
            ans = -cur
            
            #print(ans)
            if ind + 1 < len(absNums):
                
                heapq.heappush(heap, (-(ans - absNums[ind+1]), ind + 1))
                heapq.heappush(heap, (-(ans - absNums[ind+1] + absNums[ind]), ind + 1))
        
            k-=1
        return ans
            
            
            
            
            
            
            