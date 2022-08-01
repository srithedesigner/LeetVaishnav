class Solution(object):
    def uniquePaths(self, n, m):

        return math.comb(m + n - 2, m-1)
