from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        R = len(matrix)
        C = len(matrix[0])
        
        prefix = [[0] * (C + 1) for _ in range(R + 1)]
        
        for x in range(R):
            for y in range(C):
                prefix[x + 1][y] += prefix[x][y] + matrix[x][y]
        
        INF = 10 ** 20
        best = -INF
        for x1 in range(R):
            for x2 in range(x1, R):
                current = 0
                sl = SortedList()
                sl.add(0)
                
                for y in range(C):
                    current += prefix[x2 + 1][y] - prefix[x1][y]

                    index = sl.bisect_left(current - k)
                    if 0 <= index < len(sl) and best < current - sl[index]:
                        best = current - sl[index]
                    #print(y, current - k, index, sl)
                    # current - k <= prev
                    
                    sl.add(current)
                    
        return best