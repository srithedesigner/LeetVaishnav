class Solution:
    def uniquePaths(self, n, m):

        return comb(m + n - 2, min(n - 1, m - 1))