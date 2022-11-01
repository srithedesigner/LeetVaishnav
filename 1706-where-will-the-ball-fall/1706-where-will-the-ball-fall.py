class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        n, m = len(grid), len(grid[0])
        
        def atCell(x, y):
            
            #print(x, y)
            
            
            if y < 0 or y >= m:
                return -1
            
            if x == n:
                return y
        
            
            
            if grid[x][y] == 1:
                
                if y + 1 < m and grid[x][y+1] == -1:
                    return -1
                
                return atCell(x + 1, y + 1)
            
            if grid[x][y] == -1:
                
                if y - 1 >= 0 and grid[x][y-1] == 1:
                    return -1
                
                return atCell(x + 1, y - 1)
            
            return 
        
        #print(atCell(0, 0))
        return [atCell(0, i) for i in range(m)]
        
        
        
            
            