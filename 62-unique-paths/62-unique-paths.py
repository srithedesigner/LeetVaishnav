class Solution:
    def uniquePaths(self, n, m):

        number_of_paths = defaultdict(lambda : 0)

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    number_of_paths[(i, j)] = 1
                    continue
                number_of_paths[(i, j)] = number_of_paths[(i, j-1)] + number_of_paths[(i-1, j)]

        return number_of_paths[(n-1), (m-1)]