from sortedcontainers import SortedList
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        d = defaultdict(SortedList)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                
                d[i-j].add(mat[i][j])
        
        
        
        till = defaultdict(lambda : 0)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                
                p = i-j
                
                mat[i][j] = d[p][till[p]]
                till[p] += 1
                
        return mat